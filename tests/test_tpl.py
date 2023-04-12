import matplotlib.pyplot as plt
import tomplotlib as tpl
import pytest
import numpy as np


def test_import():
    import tomplotlib as tpl

    assert tpl.figure_directory is None

#makes a figure 
fig, ax = plt.subplots()
ax.scatter(np.random.uniform(50), np.random.uniform(50))


def test_saving():
    with pytest.warns(UserWarning):
        tpl.save_figure(fig, "test.png")
    # now same but with figure directory set
    tpl.figure_directory = "../figures/"
    tpl.save_figure(fig, "test.png")


def test_xy_axes():
    tpl.xy_axes(ax)
    return


def test_set_colorscheme():
    tpl.set_colorscheme(1)
    tpl.set_colorscheme("Set3")
    tpl.set_colorscheme("viridis", divisions=10)
    with pytest.raises(ValueError):
        tpl.set_colorscheme("viridis")
    tpl.set_colorscheme("viridis", divisions=10)
    return


if __name__ == "__main__":
    test_saving()
