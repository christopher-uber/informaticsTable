scripts = """
<script>
$('document').ready(fun1)
</script>
"""

#Sets graphic icon for page
icon = "road icon"

content = """
<div class="ui segment">
<div class="ui segment">

<div class="text" style="font-size:18px; text-align:center"> RoadStats Victoria is making Victoria's roads safer through Data. </div>

</div>

<div class="ui segment">

<!--
        <h1 class="ui centre aligned icon header">
          <i class="list icon" style="text-align:right"></i>
        </h1>
-->


<div class="text" style="font-size:18px; text-align:center"> Browse our large data set of Victorian road incidents <a href = "our_data.py" target="_self"> <i class="list icon" style="font-size: 75px"></i>  </a> </div>

</div>

<div class="ui segment">

<div class="text" style="font-size:18px; text-align:center"><a href = "pivot_table_form.py" target="_self"> <i class="grid layout icon" style="font-size: 75px"></i></a>  Build pivot tables from the data </div>

</div>

<div class="ui segment">

<div class="text" style="font-size:18px; text-align:center"> View our findings from the data <a href = "observations.py" target="_self"> <i class="bar chart icon" style="font-size: 75px"></i> </a> </div>

</div>
</div>

"""

from template import generate_html

page_title = "RoadStats Victoria"

scripts = """
<script>
$('document').ready(fun1)
</script>
"""


generate_html(icon, content, page_title, scripts)