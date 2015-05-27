import csv

#Make a list of column headers for the drop down menus
menu_options = []
menu_options_cat = []
data = csv.DictReader(open('../data.csv'))
for r in data:
    for key in r.keys():
        menu_options.append(key)
        try:
            float(r[key])
        except:
            menu_options_cat.append(key)
    break

# drop_down returns a string of html which creates a drop down list of options 'options' with variable 'name'
def drop_down(name, options):
    my_str = "<select name='{0}'>".format(name)

    for item in options:
        my_str += "<option value='{0}'>{0}</option>".format(item)
    my_str += "</select>"
    return my_str

def div(string):
    my_str = '<div class="field">'
    my_str += string
    my_str += "</div>"
    return my_str

page_title = "Pivot Table Builder"
br = "<br/>"

scripts = """
<script>
$('document').ready(fun1)
</script>
"""

# A list of options for filtering
filter_options = ['equal to','greater than','less than','greater than or equal to','less than or equal to', 'is anything']

# A list of options for aggregation
#aggregate_options = ['Count of','Sum of', 'Average of', 'Minimum of', 'Maximum of']

#Sets graphic icon for page
icon = "grid layout icon"

content = """
<div class="ui segment">
<form class="ui small form" action="./pivot_table_result.py" method="post">
<div class="six wide field">
"""




# Writes html for the filter category, option and value
content += div("Filter"+br+drop_down("filter", menu_options)+drop_down("filter_type", filter_options)+"""<input name="filter_val" placeholder="Filter value" type="text">"""+br*2)

# Writes hfml for row label drop down menu
content += div("Row Label"+br+drop_down("rows", menu_options)+br*2)

# Writes html for column label drop down menu
content += div("Column Label"+br+drop_down("cols", menu_options)+br*2)

# Writes html for aggregation drop down menu.. not required in spec
#content += "Aggregation"+br+drop_down("aggregate_type", aggregate_options)+drop_down("aggregate", menu_options)+br*2

# Writes html for values drop down menu - NEED TO CHANGE THIS SO ITS ONLY NUMERICAL COLUMNS
content += div("Values"+br+drop_down("aggregate", menu_options)+br*2)

content += div("<input type='checkbox' name='count' value='count'> Count")

# Writes html for submit button
content += div("""  <input type="submit" value="Apply" class="ui blue submit button"/>
  <input type="reset" value="Reset" class="ui red reset button"/>"""+br*2)



#content += """</div>
#  <input type="submit" value="Apply" class="ui purple submit button"/>
#  <input type="reset" value="Reset" class="ui purple reset button"/>
#</form>
#</div>
#"""


from template import generate_html

page_title = "Pivot Table Builder"

scripts = """
<script>
$('document').ready(fun1)
</script>
"""


generate_html(icon, content, page_title, scripts)