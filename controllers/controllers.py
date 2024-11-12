# controllers/controllers.py
from odoo import http
from odoo.http import request

class ToDoListController(http.Controller):

    @http.route('/my-template', auth='public', website=True)
    def render_template(self, **kwargs):
        return request.render('odoo-controller-XMLtemplate.my-template')
