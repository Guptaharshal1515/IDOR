"""Contract-test sketch: replace fixtures with the application's test client."""

def test_owner_allowed(client, owner, owned_invoice):
    assert client.get(f"/invoices/{owned_invoice.id}", auth=owner).status_code == 200

def test_other_tenant_denied(client, other_user, owned_invoice):
    assert client.get(f"/invoices/{owned_invoice.id}", auth=other_user).status_code in (403, 404)
