from odoo import api, fields, models, _

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.model
    def update_analytic_distribution(self):
        payments = self.env['account.payment'].search([])

        if not payments:
            return

        for payment in payments:
            journal_entries = self.env['account.move.line'].search([
                ('move_id', '=', payment.move_id.id),
                ('account_id', '!=', False)
            ])

            original_entries = self.env['account.move.line'].search([
                ('analytic_distribution', '!=', False)
            ])

            for line in journal_entries:
                for original in original_entries:
                    line.analytic_distribution = original.analytic_distribution

    def update_analytic_distribution1(self):
        payments = self.env['account.payment'].search([])
        if not payments:
            return
        for payment in payments:
            journal_entries = self.env['account.move.line'].search([
                ('move_id', '=', payment.move_id.id),
                ('account_id', '!=', False)
            ])

            original_entries = self.env['account.move.line'].search([])

            for line in journal_entries:
                for original in original_entries:
                    if original.move_id.name == line.move_id.ref and original.account_id.account_type != 'liability_payable' and line.account_id.account_type != 'liability_payable' and original.analytic_distribution:
                        line.analytic_distribution = original.analytic_distribution
                    elif original.account_id.account_type == 'liability_payable' and line.account_id.account_type == 'liability_payable' and original.move_id.name == line.move_id.ref:
                        line.analytic_distribution = original.analytic_distribution
