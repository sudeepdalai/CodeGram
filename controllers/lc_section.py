from flask import Blueprint, request
from resources.lc_section import LcSectionResource

lc_sections = Blueprint('lc_sections', __name__)


@lc_sections.route('/section', methods=['POST'])
def lc_section():
    request_data = request.get_json()
    
    card_id = request_data.get('card_id')
    collapse_id = request_data.get('collapse_id')
    heading = request_data.get('heading')

    return LcSectionResource.post(card_id, collapse_id, heading)