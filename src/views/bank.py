from flask import request, json, Response, Blueprint, g
from ..models.bank import Bank
from ..models.branch import Branch
from ..shared.authentication import Auth

bank_api = Blueprint('bank_api', __name__)


@bank_api.route('/ifsc/<string:ifsc>', methods=['GET'])
@Auth.auth_required
def bank_detail(ifsc):
    branch = Branch.get_one_branch(ifsc)
    if not branch:
        return custom_response({'error': 'branch not found'}, 404)
    return custom_response(branch.to_json(), 200)


@bank_api.route('/', methods=['GET'])
@Auth.auth_required
def get_branches():
    bank_name = request.args.get('bank')
    city = request.args.get('city')
    offset = int(request.args.get('offset', 1))
    limit = int(request.args.get('limit', 20))
    bank = Bank.get_bank(bank_name)
    branches = Branch.get_branches_with_offset(bank.id, city, offset, limit)
    if not branches:
        return custom_response({'error': 'branches not found'}, 404)
    return custom_response([branch.to_json() for branch in branches], 200)


@bank_api.route('/branches/', methods=['GET'])
@Auth.auth_required
def branches():
    bank_name = request.args.get('bank')
    city = request.args.get('city')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('limit', 20))
    bank = Bank.get_bank(bank_name)
    result = Branch.get_branches(bank.id, city, page, per_page)
    if not result:
        return custom_response({'error': 'branches not found'}, 404)
    return custom_response(jsonify_pagination(result), 200)


def jsonify_pagination(result):
    return {
        'branches': [branch.to_json() for branch in result.items],
        'total': result.total,
        'page': result.page,
        'pages': result.pages,
        'limit': result.per_page,
        'has_next': result.has_next,
        'has_prev': result.has_prev,
        'next_num': result.next_num,
        'prev_num': result.prev_num
    }


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
