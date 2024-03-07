def upload_products(instance, filename):
    return f"products/{instance.flour.title}/{filename}"


def upload_cakes(instance, filename):
    return f"cakes/{instance.cake.title}/{filename}"


def upload_flours(instance, filename):
    return f"flours/{instance.flour.title}/{filename}"