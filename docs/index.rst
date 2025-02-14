easychart
======================================
Highcharts meets python in your jupyter notebook

.. include:: fragments/badges.rst
    
Quickstart
-------------------------------------
Installing :code:`easychart` is simple with pip: 
::

    pip install easychart

Open up a new Jupyter notebook and start creating your charts:
::

    import easychart

    chart = easychart.new("column")
    chart.title = "France Olympic medals"
    chart.subtitle = "by year and by medal class"
    chart.yAxis.title.text = "medals"
    chart.categories = ["Gold","Silver","Bronze"]
    chart.plot([7, 16, 18], name=2008)
    chart.plot([11, 11, 13], name=2012)
    chart
    
.. raw:: html

    <div class="chart-container" data-filename="_static/charts/chart-1.json?v=1">loading...</div>

.. toctree::
   :maxdepth: 2
   :caption: Table of contents

   contents/introduction
   contents/examples/index
   contents/plotting-with-pandas
   contents/dimensions
   contents/themes
   contents/rendering
   contents/colormaps
   contents/API/index
   contents/about

Source
-------------------------------------
Code is hosted on `github <https://github.com/dschenck/easychart>`_