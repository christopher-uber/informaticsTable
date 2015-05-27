#Page Generator, print out HTML

from ..templates.template import generate_html

page_title = "Home Page = Aboriginal health in the 21st Century"

scripts = """
<script>
$('document').ready(fun1)
</script>
"""

content = """

<div class='ui segment'>

</div>
"""

generate_html(content, page_title, scripts)