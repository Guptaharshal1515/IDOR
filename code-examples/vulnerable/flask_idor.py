"""Illustrative anti-pattern: authentication exists, object authorization does not."""

def get_invoice(invoice_id, db):
    return db.execute("SELECT * FROM invoices WHERE id = ?", (invoice_id,)).fetchone()
