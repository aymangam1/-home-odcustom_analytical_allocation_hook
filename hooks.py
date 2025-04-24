from odoo import api, SUPERUSER_ID

def post_init_hook_function(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # vendor_bills = env['account.move'].search([('move_type', '=', 'in_invoice'), ('has_reconciled_entries', '=', False)])
    # for bill in vendor_bills:
    #     if not bill.has_reconciled_entries:
    #         # bill.split_payable_line()
    move_ids = env['account.move'].search([])
    for move in move_ids:
        if move.analytic_distribution:
            for invoice_line in move.invoice_line_ids:
                if not invoice_line.analytic_distribution:
                    invoice_line.analytic_distribution = move.analytic_distribution
            for line_id in move.line_ids:
                if not line_id.analytic_distribution:
                    print(line_id.name)
                    line_id.analytic_distribution = move.analytic_distribution
    payment_ids = env['account.payment'].search([])
    for payment in payment_ids:
        payment.update_analytic_distribution1()










