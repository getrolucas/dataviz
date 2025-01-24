def y_ticks_formatter(x, pos):
    if x >= 1e6:
        return f'{x*1e-6:.0f}M'
    
    if x >= 1e3:
        return f'{x*1e-3:.0f}K'
    
    return f'{x:.0f}'