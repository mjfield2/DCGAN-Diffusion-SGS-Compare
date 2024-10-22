import skgstat as skg

def experimental_variogram(coords, field, kwargs):
    vario = skg.Variogram(coords, field, **kwargs)
    return vario.experimental