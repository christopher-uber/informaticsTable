#Templates

# Hugo suggestions:
#        Add a graphic below the menu bar ( eg a road texture)
#        Add different pictures/icons per page (eg a pencil for the table builder, a car for the homepage or something like that)
#        Add a graphic/thicker bar at the bottom of each page (maybe just the same as the above graphic bar, like a road texture)
#        


def head_tag(scripts="", pagetitle="Road to Safety"):
    #<html>
    #<head> content, meta content </head>
    #<script> tag content, scripts optional arguement - scripts variable
    # should contain <script> tags
    # that contains a multi line string for JS stuff to go here
    #CSS/Semantic link and any other style sheets
    html = """
    <html>
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
        <script src="http://code.highcharts.com/highcharts.js"></script>
        <script src="http://code.highcharts.com/highcharts-more.js"></script>
        <script src="http://code.highcharts.com/modules/exporting.js"></script>
        
    
      <link rel="stylesheet" type="text/css" href="./static/style/css/style.css" />
      <link rel="stylesheet" type="text/css" href="./static/style/css/dist/semantic.css" />
        <title>{0}</title>
        <base href="./" target="_blank">
        <meta charset="UTF-8">
        <meta name="description" content="INFO20002 Project examining a dataset">
        <meta name="keywords" content="csv,data,info20002">
        <meta name="author" content="Hugo Edwards, Anuja Ratwatte, Christopher Uber">
        """.format(pagetitle)
    html += """
        {0}
    </head>
    """.format(scripts)

    return html

def menu():
    html = '''
    <body>
    
    <header>
    <nav>
    <div class="ui inverted blue menu">
          <a href="home.py" target="_self" class="item" style="font-size:24px"><i class="road icon"></i>RoadStats Victoria</a>

          <a href="our_data.py" target="_self" class="item">Our Data</a>
          <a href="pivot_table_form.py" target="_self" class="item">Pivot Table</a>
          <!-- <a href="graphs.py" target="_self" class="item">Graphs</a> -->
          <a href="observations.py" target="_self" class="item">Findings</a>
          
      <!--<div class="right menu">
          <div class="item">Making Victoria's roads safer with data</div> -->
     </div>
    </div>
    </nav>
    </header>'''

    #</body>
    #menu links
    return html


def header(icon, pagetitle="RoadStats Victoria"):

    #Page Bannerguement to change the title of the page
    #optional arguement to replace the banner title
    #<div id="content"> to lead to content section
    html = '''
    <div class='ui segment' >
        <h1 class="ui center aligned icon header">
          <i class="'''+icon+'''"></i>
              {0}
        </h1>
    </div>

    <div id="content">
    '''.format(pagetitle)

    return html


def footer():
    #</div>
    #About us
    #SiteMap
    #</body>
    #<html>
    html = '''
    </div>
    </div>
    <footer>
      <div class="ui horizontal divider">
    <br>
         <i class="idea icon"></i>
    <br>
    <br>
         <div style="text-transform: none">RoadStats Victoria is making Victoria's roads safer with data. This website has been designed by Anuja Ratwatte, Chris Uber and Hugh Edwards</div>
      </div>
    </footer>
    </body>
    </html>
    '''
    return html

def generate_html(icon, content, pagetitle="", scripts=""):
    """ Takes scripts (optional) and content as variables containing
    strings of html code to be printed and builds the html file for 
    printing """
    try:
        print "Content-Type: text/html"
        print "\n"
        print head_tag(scripts, pagetitle) if pagetitle else head_tag(scripts)
        print menu()
        print header(icon, pagetitle) if pagetitle else header(icon)
        print content
        print footer()
        return ""
    except Exception as e:
        return e

