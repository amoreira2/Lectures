def SR(R,W=[],freq=12):
    if np.empty(W):
        sr=R.mean()/R.std()*freq**0.5
    else:
        r=R@W
        sr=r.mean()/r.std()*freq**0.5
    return sr