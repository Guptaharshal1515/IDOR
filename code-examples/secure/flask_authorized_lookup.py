"""Illustrative secure shape; policy details belong to the application."""

def get_invoice(invoice_id, current_user, db):
    row = db.execute("SELECT * FROM invoices WHERE id = ? AND tenant_id = ?", (invoice_id, current_user.tenant_id)).fetchone()
    if row is None:
        raise LookupError("not found or not authorized")
    return row
