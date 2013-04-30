"""Unit tests for correlograms view."""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import os

import numpy as np
import numpy.random as rnd
import pandas as pd

from klustaviewa.io.tests.mock_data import (setup, teardown,
        nspikes, nclusters, nsamples, nchannels, fetdim, ncorrbins, 
        create_baselines, create_correlograms)
from klustaviewa.io.loader import KlustersLoader
from klustaviewa.io.selection import select
from klustaviewa.io.tools import check_dtype, check_shape
from klustaviewa.utils.userpref import USERPREF
from klustaviewa.views import CorrelogramsView
from klustaviewa.views.tests.utils import show_view, get_data


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
def test_correlogramsview():
    keys = ('clusters_selected,cluster_colors').split(',')
           
    data = get_data()
    kwargs = {k: data[k] for k in keys}
    
    kwargs['correlograms'] = create_correlograms(kwargs['clusters_selected'], 
        ncorrbins)
    kwargs['baselines'] = create_baselines(kwargs['clusters_selected'])
    
    kwargs['operators'] = [
        lambda self: (self.close() 
            if USERPREF['test_auto_close'] != False else None),
    ]
    
    # Show the view.
    show_view(CorrelogramsView, **kwargs)
    
    