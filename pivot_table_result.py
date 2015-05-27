import sqlite3
import time
import cgi
from template import generate_html



class UserInput():
    """Class for any user input comming into the form
    This is effectively part of the model from where we 
    draw our data from"""

    class form():
        """This class is for data coming in from the form on the previous page 
        Need to replace spaces to match DB cols and do some basic filtering"""

        cgi_store = cgi.FieldStorage()
        row = cgi_store['rows'].value.strip().replace(" ", "_")
        column = cgi_store['cols'].value.strip().replace(" ", "_")
        aggregate = cgi_store['aggregate'].value.strip().replace(" ", "_")
        filter_column = cgi_store['filter'].value.strip().replace(" ", "_")
        filter_operation_string = cgi_store["filter_type"].value
        blank = ''
        form_input = cgi_store['filter_val'].value if 'filter_val' in cgi_store.keys() else ""
        count = cgi_store['count'].value if 'count' in cgi_store.keys() else ""

        def filter_operation(self):
            """
            Converts between text and mathematical symbol for the filter type
            """
            transforms = {"equal to":"=", "less than":"<", "greater than":">", "less than or equal to":"<=", "greater than or equal to":">=", "is anything":""}
            return transforms[self.filter_operation_string]

        def filter_string(self):
            if self.filter_operation():
                return "{0} {1} {2}".format(self.filter_column, self.filter_operation(), self.filter_input())
            else:
                return ""

        def filter_input(self):
            if self.form_input:
                try:
                    float(self.form_input)
                    return self.form_input
                except:
                    return "'{0}'".format(self.form_input.lower())
            else:
                return ""
            
        def __unicode__(self):
            """
            if the object is ever called by itself, maybe more meaningful
            """
            return cgi_store
            


    def __unicode__(self):
        """
        UserInput isn't valid on its own
        """
        return "Invalid Call"

UserInput_form = UserInput.form() #bind form to instance
    
class sql_database():
    """docstring for sql_database"""

    database_name = 'crash_data.db'
    connection = sqlite3.connect(database_name)
    sql_cursor = connection.cursor()

    def __unicode__(self,):
        return database_name

def custom_sort(input):
    """
    Sorts for days of the week and general sort
    """
    week = {"monday":1, "tuesday":2, u"wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    if input[0] in week.keys():
        return sorted(input, key=lambda x: week[x])
    return sorted(input)

def gather_data(chosen_x_attribute, chosen_y_attribute, aggregate_val, filter_string, sql_cursor):
    """
     Does the sql querying from the database. Returns a dataobject to pass on to the rest of the program
    Completes the model section
    """
    
    def bin(input, number):
        """
        seperates an lst input into a numbe o
        """
        num_of_bins = number
        minval = min(input)
        maxval = max(input)
        bincounts = [0 for i in range(num_of_bins+1)] #initalize bins
        for value in input:
            b = int((value - minv) / (maxv - minv) * num_of_bins)
            bincounts[b] += 1
        return bincounts
    
    def sql_unique_vals(column):
        """
        Selects all unique values if the column is strings, otherwise puts it into bins.
        """
        output = []
        float_col = False
        for sql_row in sql_database.sql_cursor.execute("SELECT DISTINCT {0} FROM crash_data;".format(column)):
            try:
                if sql_row[0]: #check if not blank
                    float(sql_row[0]) #see if it is a number
                    output.append(sql_row[0])                    
            except:
                if sql_row[0]:
                    output.append(sql_row[0])
        """
        # Creates bins if column is floats.
        if float_col and len(output)>10:
            bins = bin(output, 10) #create a list to hold the Quartiles
            output = []
            for number in bins: # Add these to the output
                output.append(str(number))
        
           if time convert to number of seconds, bin then convert back?
           """
            
        return output


    def main_sql(row_lst, col_lst):   
    """
    returns the values for the datamatrix object
    """
        def sql_statement(row_val, col_val):
        """
        Although only used once, this is spun out into a formula for seperation of concerns reasoning
        so someone could work on the SQL independant of the rest of function
        """
            if UserInput_form.filter_string():
                sql_statement_output = "SELECT {0} FROM crash_data WHERE {1} = '{2}' AND {3} = '{4}' AND {5};".format(UserInput_form.aggregate, UserInput_form.row, row_val, UserInput_form.column, col_val, UserInput_form.filter_string())
            else:
                sql_statement_output = "SELECT {0} FROM crash_data WHERE {1} = '{2}' AND {3} = '{4}';".format(UserInput_form.aggregate, UserInput_form.row, row_val, UserInput_form.column, col_val)
            return sql_statement_output

        data_matrix = {}
        for row in custom_sort(row_lst):
            if row:
                data_matrix[row] = []
                for col in custom_sort(col_lst):
                    if col:
                        sql_output = sql_database.sql_cursor.execute(sql_statement(row, col))
                        row_sum = 0
                        for sql_row in sql_output:
                            if UserInput_form.count:
                                row_sum += 1
                            else:
                                row_sum += sql_row[0]
                        data_matrix[row].append(row_sum)
        return data_matrix
    

    row_uniques = sql_unique_vals(UserInput_form.row)
    col_uniques = sql_unique_vals(UserInput_form.column)

    output = {}
    output['data_matrix'] = main_sql(row_uniques, col_uniques)
    output['rows'] = row_uniques
    output['cols'] = col_uniques
    return output

def error():
    """
    Controller? Checks the users input for validity
    In a better model, this would take in the model object and then send it to the view
    but this isn't needed in the flat file version
    """
    def isint(s):
        try:
            int(s)
            return True
        except:
            return False
        
    for row in sql_database.sql_cursor.execute("SELECT typeof({0}),typeof({1}),typeof({2}),typeof({3}) FROM crash_data;".format(UserInput_form.filter_column, UserInput_form.row, UserInput_form.column, UserInput_form.aggregate)):
        filtercol_type = row[0]
        chosenrow_type = row[1]
        chosencol_type = row[2]
        chosenagg_type = row[3]
        filter_string = UserInput_form.filter_input()
        filter_operation = UserInput_form.filter_operation()
        break #only need to check once

    blank = '' # This is the check for if the user chooses 'anything' as the filter operation
    
    # Error handling boolean values
    
    # Configuration to filter by a column of strings
    filter_config_1 = ( (filtercol_type == 'text') and (filter_operation == '=') and ( (filter_string) and (not isint(filter_string)) ) )
    
    # Configuration to filter by 'anything'. The check to see if the chosen operation is blank is our indicator that the user has chosen the 'anything' option.
    filter_config_2 = (((filtercol_type == 'text') or (filtercol_type == 'integer')) and (not filter_operation) and (not filter_string))
    
    # Configuration to filter by a column of integers.
    filter_config_3 = ( (filtercol_type == 'integer') and (filter_operation) and isint(filter_string) ) 
    
    # Boolean variable to combine all the above filter checks
    filter_good = (filter_config_1 or filter_config_2 or filter_config_3)

    # String comparison of the chosen column and row labels
    column_row_diff = UserInput_form.column != UserInput_form.row
    
    # test for text based values
    values = chosenagg_type == 'integer' if not UserInput_form.count else True

     
    if (filter_good and column_row_diff and values):
        return True
    else:
        return False

def redirect():
    """
    Generates a page redirecting the user in case of an error
    Start of the View
    """
    html = """Content-Type: text/html \n\n
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="../static/style/css/dist/semantic.css" />
    <title>Form Error</title>
    <meta http-equiv="refresh" content="5; url=./pivot_table_form.py" />
    </head>
    <body>
        <header>
    <nav>
    <div class="ui inverted blue menu">
          <a href="home.py" target="_self" class="item" style="font-size:24px"><i class="road icon"></i>SafeRoads Victoria</a>

          <a href="our_data.py" target="_self" class="item">Our Data</a>
          <a href="pivot_table_form.py" target="_self" class="item">Pivot Table</a>
          <a href="graphs.py" target="_self" class="item">Graphs</a>
          <a href="observations.py" target="_self" class="item">Findings</a>
          
      <div class="right menu">
          <div class="item">Making Victoria's roads safer with data</div>
     </div>
    </div>
    </nav>
    </header>
    <div class="ui segment">
    Error. Incompatible filter options
    </div>
    </body>
    </html>"""
    return html
    
    
def html_output(data):
    """
    Generates the view for the table, interhits the template from template.py
    and then extends it with content, in this case the table,
    """
    icon = "road"
    page_title = "Pivot Table"

    min_val = min(min(data['data_matrix'].itervalues()))
    max_val = max(max(data['data_matrix'].itervalues()))
    
    scripts = ""

    row_title = UserInput_form.row.replace("_", " ").title()
    col_title = UserInput_form.column.replace("_", " ").title()
    val_title = UserInput_form.aggregate.replace("_", " ").title()
    filter_title = "Filtered by: '{0} {1} {2}'".format(UserInput_form.filter_column.replace("_", " ").title(), UserInput_form.filter_operation_string, UserInput_form.filter_input().title())
    
    content = """
    <div class='ui segment'>
    <h1>Comparing {0} against {1} for the {4} of "{2}"</h1>
    <h3>{3}</h3>
    <br>
    <h3 style="text-align: center;">{1}</h3>
    <h3 style="transform: rotate(90deg); transform-origin: left top 0; position: relative; top: 150; left: 25;">{0}</h3>
    <div style="padding-left: 60px;">
    <table class="ui definition table" style="">
    <thead>
    <tr><th></th>""".format(row_title, col_title, val_title, filter_title, ("sum" if not UserInput_form.count else "count"))
    for col in custom_sort(data['cols']):
        content += "<th>{0}</th>".format(str(col).title())
    content += "<th>Total</th>"
    content += """</tr></thead>
    <tbody>"""

    # The cell values
    for row in custom_sort(data['rows']):
        content += """<tr>
         <td>{0}</td>""".format(row.title())
        for col_item in data['data_matrix'][row]:
            content += """<td style="background-color: hsl(210,50%,{0}%)">{1}</td>""".format(str((1-(float(col_item)-min_val)/(max_val-min_val+1))*50+50),col_item)
        content += "<td><strong>{0}</strong></td>".format(sum(data['data_matrix'][row]))
        content += "</tr>"
    content += """<tr>
    <td>Total</td>"""

    # The column totals
    for col in range(0,len(data["cols"])):
        total = 0
        for row in data['rows']:
            total += data['data_matrix'][row][col]
        content += "<td><strong>{0}</strong></td>".format(total)

    content += "<td> Grand Total </td>"
    content += """
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    
    <div class="ui segment">

    <h3 style="text-align: center"> Colour Legend </h3>

    <table style="width:100%; border: 1px solid black">
      <tr>"""
    
    # colour legend below the table
    max_i = 100

    for i in range(max_i+1):
        cell_text = ""
        align = "left"
        if i==0:
            cell_text = str(min_val)
        elif i==max_i:
            cell_text = str(max_val)
            align = "right"
        content += """<td style="text-align:"""+align+"""; background-color: hsl(210,50%,"""+str((1-(float(i))/(max_i))*50+50)+"""%)">"""+cell_text+"""</td>"""
        
    content += """
      </tr>
    </table>
    </div>
    

    """

    return generate_html(icon, content, page_title, scripts="")

def main():
    """
    Runs the collection of elements to generate the page
    """
    if not error():
        return redirect()
    data = gather_data(UserInput_form.row, UserInput_form.column, UserInput_form.aggregate, UserInput_form.filter_string, sql_database.sql_cursor)
    return html_output(data)

print main()