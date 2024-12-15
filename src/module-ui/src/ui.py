def run_streamlit():
   import streamlit as st

   st.set_page_config(layout="wide")
   if 'total_points' not in st.session_state:
      st.session_state.total_points = 0
      st.session_state.con_sql_lvl1_getstarted_points = 0
      st.session_state.con_sql_lvl1_datamart_points = 0
      st.session_state.con_sql_lvl1_joinsviews_points = 0
      st.session_state.con_sql_lvl1_warehousesizing_points = 0
      st.session_state.con_sql_lvl2_dynamictables_points = 0
      st.session_state.con_sql_lvl2_dynamictablesnext_points = 0
      st.session_state.con_inter_warehousesizing_1 = 0
      st.session_state.con_inter_warehousesizing_2 = 0
      st.session_state.con_inter_dynamictable_1 = 0
      st.session_state.con_inter_dynamictable_2 = 0
      st.session_state.con_adv_streamlitgame_1 = 0


   st.title(":blue[Snowflake Games]")

   CON_POINTS0 = 0
   CON_POINTS1 = 1
   CON_POINTS2 = 2
   CON_POINTS3 = 3
   CON_POINTS4 = 4
   CON_POINTS5 = 5
   CON_POINTS6 = 6


   def displaytext_total_game_points():
      st.session_state.total_points = st.session_state.con_sql_lvl1_getstarted_points
      st.session_state.total_points += st.session_state.con_sql_lvl1_datamart_points
      st.session_state.total_points += st.session_state.con_sql_lvl1_joinsviews_points
      st.session_state.total_points += st.session_state.con_sql_lvl1_warehousesizing_points
      st.session_state.total_points += st.session_state.con_sql_lvl2_dynamictables_points 
      st.session_state.total_points += st.session_state.con_sql_lvl2_dynamictablesnext_points 
      st.session_state.total_points += st.session_state.con_inter_warehousesizing_1 
      st.session_state.total_points += st.session_state.con_inter_warehousesizing_2 
      st.session_state.total_points += st.session_state.con_inter_dynamictable_1 
      st.session_state.total_points += st.session_state.con_inter_dynamictable_2 
      st.session_state.total_points += st.session_state.con_adv_streamlitgame_1
      st.markdown(f':orange[*Total Score All Games = {st.session_state.total_points}*]')

   def displaytext_correct(score):
      st.markdown(f':green[*Correct!  (score={score})*]')

   def displaytext_tryagain(score):
      st.markdown(f':red[**Try again**  (score={score})]')

   def displaycode(syntax_text):
      st.code(syntax_text, language="SQL")

   def displaytext_pass_game():
      st.markdown(f':blue[**CONGRATULATIONS! YOU WON THIS GAME!**]')

   def displaytext_pass_level():
      st.markdown(f':green[**\nCONGRATULATIONS! YOU ALSO PASSED THIS LEVEL!**]')

   def display_snowflake_docs_url():
      st.markdown("""*Snowflke documentation command reference - https://docs.snowflake.com/en/sql-reference-commands*""")

   def display_snowflake_dynamic_tables_url():
      st.markdown("""*Snowflke documentation - https://docs.snowflake.com/en/user-guide/dynamic-tables-create*""")

   def display_snowflake_dynamic_tables_next_url():
      st.markdown("""*Snowflke documentation - https://docs.snowflake.com/en/user-guide/dynamic-tables-about*""")

   def display_snowflake_streamlit_docs_url():
      st.markdown("""*[Snowflake documentation - https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit]*""")

   def waschanged(key):
      st.info(st.session_state[key])

   #--------------------------------------------------------------------
   # SIDEBAR #

   with st.sidebar:
      st.subheader(""":blue[Interactive Learning Games]""")
      st.write('')
      
      level_selected = st.selectbox(
         '**Select a game level:**',
         ['',
            'SQL - Level 1',
            'SQL - Level 2',
            'Puzzles - Intermediate',
            'Streamlit - Python Advanced'
         ]
      )

      level1_games = ['',
            'Database Setup',
            'Data Marts for Beginners',
            'SQL Joins and Views',
            'Pick the right warehouse size'
         ]

      level2_games = ['',
            'Create a Dynamic Table',
            'Next steps with Dynamic Tables'
         ]

      intermediate_games = ['',
            'Warehouse Sizing Challenge #1',
            'Optimizing Queries #1',
            'Design a Dynamic Table #1',
            'Design a Dynamic Table #2'
         ]

      advanced_games = ['',
            'Streamlit - Create a question game'
         ]

      if level_selected == 'SQL - Level 1':
         game_selected = st.selectbox(
         '**Select a game to play:**',
         level1_games
         )
      elif level_selected == 'SQL - Level 2':
         game_selected = st.selectbox(
         '**Select a game to play:**',
         level2_games
         )
      elif level_selected == 'Puzzles - Intermediate':
         game_selected = st.selectbox(
         '**Select a game to play**',
         intermediate_games
         )
      elif level_selected == 'Streamlit - Python Advanced':
         game_selected = st.selectbox(
         '**Select a game to play:**',
         advanced_games
         )
      else:
         game_selected = st.selectbox(
         '**Select a game to play:**',
         ['']
      )

      if game_selected == 'Database Setup':
         st.session_state.active_game_name = 'con_sql_lvl1_getstarted'
      elif game_selected == 'Data Marts for Beginners':
         st.session_state.active_game_name = 'con_sql_lvl1_datamart'
      elif game_selected == 'SQL Joins and Views':
         st.session_state.active_game_name = 'con_sql_lvl1_joinsviews'
      elif game_selected == 'Pick the right warehouse size':
         st.session_state.active_game_name = 'con_sql_lvl1_warehousesizing'
      elif game_selected == 'Create a Dynamic Table':
         st.session_state.active_game_name = 'con_sql_lvl2_dynamictables'
      elif game_selected == 'Next steps with Dynamic Tables':
         st.session_state.active_game_name = 'con_sql_lvl2_dynamictablesnext'
      elif game_selected == 'Warehouse Sizing Challenge #1':
         st.session_state.active_game_name = 'con_inter_warehousesizing_1'
      elif game_selected == 'Optimizing Queries #1':
         st.session_state.active_game_name = 'con_inter_queryoptimizing_1'
      elif game_selected == 'Design a Dynamic Table #1':
         st.session_state.active_game_name = 'con_inter_dynamictable_1'
      elif game_selected == 'Design a Dynamic Table #2':
         st.session_state.active_game_name = 'con_inter_dynamictable_2'
      elif game_selected == 'Streamlit - Create a question game':
         st.session_state.active_game_name = 'con_adv_streamlitgame_1'
      else:
         st.session_state.active_game_name = None

      st.write('')
      st.write('')
      st.markdown("**:blue[Game Requirements]**")
      st.markdown(":blue[1. Database Permissions:]")
      st.markdown("* SQL Level 1 - create database objects  \n* SQL Level 2 - create dynamic tables")
      st.markdown(":blue[2. Trial account edition:]")
      st.markdown("* Enterprise Edition trial account")
      st.markdown(":blue[3. Snowflake role context:]")    
      st.markdown("* Execute SQL Worksheet scripts and create Streamlit apps as the SYSADMIN role")
      st.write('')
      show_points = st.text_input(":orange[Total Game Points]", value=st.session_state.total_points, key='txt_total_points')
      st.button("Update points")

   #--------------------------------------------------------------------
   # con_sql_lvl1_getstarted #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl1_getstarted':
         
         st.subheader(":blue[Level 1 - Database Setup]")
         st.markdown(
               """
               Each correct answer builds your SQL script and your score!  At the end, click the Worksheets button from the left navigation bar and execute the SQL script
               that you build along the way in a SQL Worksheet and see your creation in Snowflake!  Select a role and a warehouse in order to execute your script. \n
               """
         )
         display_snowflake_docs_url()
         st.markdown("""---""")
      
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         inp_Q001 = st.selectbox(
               '**Which statement will add a new database named "analytics" to Snowflake?**',
               ['',
               'database.add = "analytics";',
               'create database = "analytics";',
               'create database analytics;']
         )
         
         if inp_Q001 != 'create database analytics;' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)            
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
               displaycode(inp_Q001)
         
               inp_Q002 = st.selectbox(
                  '**Which statement will add a new schema named "metrics"?**',
                  ['',
                  'create schema as metrics;',
                  'create schema metrics;',
                  'analytics.add = "metrics";']
               )
         
               if inp_Q002 != 'create schema metrics;' and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
                  displaycode(inp_Q002)
         
                  inp_Q003 = st.selectbox(
                     '**Which statement activates a database or schema to be the current context that commands will execute in?**',
                     ['',
                        'use schema = metrics;',
                        'use metrics;',
                        'use schema metrics;']
                  )
               
                  if inp_Q003 != 'use schema metrics;' and inp_Q003 != '':
                     displaytext_tryagain(CON_POINTS2)
                  elif inp_Q003 != '' or logic_override:
                     displaytext_correct(CON_POINTS3)
                     displaycode(inp_Q003)
               
                     ctr_Q002 = st.container()
         
                     opts_Q004 = ctr_Q002.multiselect("**Select the commands to establish a database and schema and activate them in the order they need to be executed.  Use all selections.**",
                           ['create schema metrics;', 'use database analytics;', 'create database analytics;','use schema metrics;'])
         
                     if len(opts_Q004) == 0:
                           st.write('')
                     elif len(opts_Q004) > 0 and len(opts_Q004) < 4:
                           st.write(':green[*Select all items in proper sequence for score*]')
                     elif len(opts_Q004) == 4:
                           if opts_Q004[0] != 'create database analytics;' \
                           or opts_Q004[1] != 'use database analytics;'\
                           or opts_Q004[2] != 'create schema metrics;'\
                           or opts_Q004[3] != 'use schema metrics;':
                              displaytext_tryagain(CON_POINTS3)
                           else:
                              displaytext_correct(CON_POINTS4)
                              displaytext_pass_game()
                              st.markdown(f':blue[Execute the following script in a SQL Worksheet as sysadmin to create a database with your custom schema.  Refresh the object explorer when done to see the database and schema.]')
                              displaycode(opts_Q004[0] + " \n" + opts_Q004[1] + " \n" + opts_Q004[2] + " \n" + opts_Q004[3])
                              st.session_state.con_sql_lvl1_getstarted_points = CON_POINTS4
                              displaytext_total_game_points()

   #--------------------------------------------------------------------
   # con_sql_lvl1_datamart #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl1_datamart':

         st.subheader(":blue[Level 1 - Data Marts for Beginners]")
         st.markdown(
               """
               Each correct answer builds your score!
               """
         )
         display_snowflake_docs_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         inp_Q001 = st.selectbox(
               "*Which of these table names does not belong as a standard dimension or fact table in a 'star schema' data mart design?*",
               ['',
               'dim_product_types',
               'products',
               'fact_metrics',
               'fact_product_returns']
         )
         
         if inp_Q001 != 'products' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
               displaycode(inp_Q001)
         
               inp_Q002 = st.selectbox(
                  "*How is data typically loaded into a data mart?*",
               ['',
               'Directly from source data repositories',
               'From a database where a copy of the raw data is ingested into',
               'From a staging database where additional transformed data was incorporated',
               'From a second copy of the data mart database that was first created for disaster recovery']
               )
         
               if inp_Q002 != "From a staging database where additional transformed data was incorporated" and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
                  displaycode(inp_Q002)
         
                  inp_Q003 = st.selectbox(
                     "*How many fact tables are typically in a data mart query?*",
                  ['',
                  '1',
                  '2',
                  '4',
                  '11']
                  )
               
                  if inp_Q003 != "1" and inp_Q003 != '':
                     displaytext_tryagain(CON_POINTS2)
                  elif inp_Q003 != '' or logic_override:
                     displaytext_correct(CON_POINTS3)
                     displaycode(inp_Q003)
                     
                     inp_Q004 = st.selectbox(
                           "*What is a data mart design model called that contains multiple fact tables?*",
                     ['',
                        'Star',
                        'Snowflake',
                        'Constellation',
                        'Galaxy']
                     )
         
                     if inp_Q004 != "Galaxy" and inp_Q004 != '':
                           displaytext_tryagain(CON_POINTS3)
                     elif inp_Q004 != '' or logic_override:
                           displaytext_correct(CON_POINTS4)
                           displaycode(inp_Q004)
                           
                           inp_Q005 = st.selectbox(
                              "*What field does not belong in a fact table of key and metric values?*",
                           ['',
                           'year_over_year_growth_percent',
                           'product_count',
                           'product_type_id',
                           'product_description',
                           'avg_order_amount']
                           )
            
                           if inp_Q005 != "product_description" and inp_Q005 != '':
                              displaytext_tryagain(CON_POINTS4)
                           elif inp_Q005 != '' or logic_override:
                              displaytext_correct(CON_POINTS5)
                              displaycode(inp_Q005)
                              print("")
                              
                              ctr_Q002 = st.container()
                  
                              opts_Q006 = ctr_Q002.multiselect("**What are the four stages of database design?  Put them in the order they are conducted.**",
                                    ['Statistical', 'Logical', 'Conceptual','Transformational','Physical'])
                  
                              if len(opts_Q006) == 0:
                                 st.write('')
                              elif len(opts_Q006) > 0 and len(opts_Q006) < 4:
                                 st.write(':green[*Select all four items in proper sequence for score*]')
                              elif len(opts_Q006) > 4 :
                                 st.write(':green[*You have selected too many items*]')
                              elif len(opts_Q006) == 4:
                                 if opts_Q006[0] != 'Conceptual' \
                                 or opts_Q006[1] != 'Logical' \
                                 or opts_Q006[2] != 'Physical' \
                                 or opts_Q006[3] != 'Transformational':
                                       displaytext_tryagain(CON_POINTS5)
                                 else:
                                       displaytext_correct(CON_POINTS6)
                                       displaycode(opts_Q006[0] + " \n" + opts_Q006[1] + " \n" + opts_Q006[2] + " \n" + opts_Q006[3])
                                       displaytext_pass_game()
                                       st.session_state.con_sql_lvl1_datamart_points = CON_POINTS6
                                       displaytext_total_game_points()

   #------------------------------------------------------------------
   # con_sql_lvl1_joinsviews #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl1_joinsviews':

         st.subheader(":blue[Level 1 - SQL Joins and Views]")
         st.markdown(
               """
               Each correct answer builds your SQL script and your score!  At the end, click the Worksheets button from the left navigation bar and execute the SQL script
               that you build along the way in a SQL Worksheet and see your creation in Snowflake!  Select a role and a warehouse in order to execute your script. \n
               """
         )
         st.markdown("""*:blue[This game depends on the preliminary scripts to be ran first:]*""")
         st.markdown("*:blue[Level 1 - Database Setup]*")  
         display_snowflake_docs_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         inp_Q001 = st.selectbox(
               '**Which statement will add a new lookup table to an existing database with a list of types for products and add new rows of data to the table?**',
               ['',
               'database.add.table = "dim_product_types";',
               'create table dim_product_types (product_type_id int, product_type_name string);',
               'create dim_product_types as table;']
         )
         
         if inp_Q001 != 'create table dim_product_types (product_type_id int, product_type_name string);' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
               displaycode(inp_Q001)
         
               inp_Q002 = st.selectbox(
                  '**Which statement will add new rows of data to your table?**',
                  ['',
                  "insert into dim_product_types (1,'bike', 2,'motorcycle', 3,'truck');",
                  "dim_product_types.add (1,'bike), (2,'motorcycle), (3,'truck');",
                  "insert into dim_product_types values(1,'bike');" + \
         "insert into dim_product_types values(2,'motorcycle');" + \
         "insert into dim_product_types values(3,'truck');"]
               )
         
               if inp_Q002 != "insert into dim_product_types values(1,'bike');" + \
         "insert into dim_product_types values(2,'motorcycle');" + \
         "insert into dim_product_types values(3,'truck');" and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
                  displaycode(inp_Q002.replace(';',';\n'))
         
                  inp_Q003 = st.selectbox(
                     '**Which statement will create and populate a second table with metric data?**',
                     ['',
                        "create fact_metrics (metric_id, product_type_id, metric_date, product_count, product_amount);\
                        insert into fact_metrics (1, 1, '2024-08-17',241,305867);",
                        "create table fact_metrics (metric_id int, product_type_id string, metric_date date, product_count int, product_amount number(18,6));" +\
         "insert into fact_metrics values(1, 1, '2024-08-17',241,305867);"]
                  )
               
                  if inp_Q003 != "create table fact_metrics (metric_id int, product_type_id string, metric_date date, product_count int, product_amount number(18,6));" +\
         "insert into fact_metrics values(1, 1, '2024-08-17',241,305867);" and inp_Q003 != '':
                     displaytext_tryagain(CON_POINTS2)
                  elif inp_Q003 != '' or logic_override:
                     displaytext_correct(CON_POINTS3)
                     inp_Q003 = "create table fact_metrics (metric_id int, product_type_id string, metric_date date, product_count int, product_amount number(18,6));" +\
         "insert into fact_metrics values(1, 1, '2024-08-17',241,305867);" + \
         "insert into fact_metrics values(2, 3, '2024-08-17',3,180004);" +\
         "insert into fact_metrics values(3, 1, '2024-08-18',14,18540);"
                     displaycode(inp_Q003.replace(';',';\n'))
               
                     ctr_Q002 = st.container()
         
                     opts_Q004 = ctr_Q002.multiselect("**Select the commands to establish a view joining data from the two tables in the order they need to be executed.  Use all selections.**",
                           ['create view product_metrics_vw as', 'from fact_metrics f inner join dim_product_types p', 'on f.product_type_id = p.product_type_id;','select product_type_name, product_count, product_amount, metric_date'])
         
                     if len(opts_Q004) == 0:
                           st.write('')
                     elif len(opts_Q004) > 0 and len(opts_Q004) < 4:
                           st.write(':green[*Select all items in proper sequence for score*]')
                     elif len(opts_Q004) == 4:
                           if opts_Q004[0] != 'create view product_metrics_vw as' \
                           or opts_Q004[1] != 'select product_type_name, product_count, product_amount, metric_date'\
                           or opts_Q004[2] != 'from fact_metrics f inner join dim_product_types p'\
                           or opts_Q004[3] != 'on f.product_type_id = p.product_type_id;':
                              displaytext_tryagain(CON_POINTS3)
                           else:
                              displaytext_correct(CON_POINTS4)
                              displaycode(opts_Q004[0] + " \n" + opts_Q004[1] + " \n" + opts_Q004[2] + " \n" + opts_Q004[3])
         
                              inp_Q005 = st.selectbox(
                                       '**Which statement will only retrieve bikes from your table sorted by most recent date?**',
                                       ['',
                                       "select * from product_metrics_vw;",
                                       "select * from product_metrics_vw sorted by latest(metric_date);",
                                       "select * from product_metrics_vw" + \
         "where product_type_name != 'truck'" + \
         "order by metric_date desc;"]
                                 )
                              
                              if inp_Q005 != "select * from product_metrics_vw" + \
         "where product_type_name != 'truck'" + \
         "order by metric_date desc;" and inp_Q005 != '':
                                 displaytext_tryagain(CON_POINTS1)
                              elif inp_Q005 != '' or logic_override:
                                 displaytext_correct(CON_POINTS5)
                                 displaytext_pass_game()
                                 st.markdown(f':blue[Execute the following script in a SQL Worksheet as sysadmin to create all objects in your database.  Use the sysadmin role for all your scripts.  Refresh the object explorer when done to see the table and view objects.]')
                                 displaycode(inp_Q001 + "\n\n" + inp_Q002.replace(';',';\n') + "\n\n" + inp_Q003.replace(';',';\n') + "\n\n" + \
                                 opts_Q004[0] + " \n" + opts_Q004[1] + " \n" + opts_Q004[2] + " \n" + opts_Q004[3] + " \n\n" +  inp_Q005.replace('_vw','_vw\n').replace("k'","k'\n"))
                                 st.session_state.con_sql_lvl1_joinsviews_points = CON_POINTS5
                                 displaytext_total_game_points()


   #--------------------------------------------------------------------
   # con_sql_lvl1_warehousesizing #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl1_warehousesizing':
               
         st.subheader(":blue[SQL Level 1 - Pick the right warehouse size]")
         st.markdown(
               """
               Each correct answer builds your SQL script and your score!  At the end, click the Worksheets button from the left navigation bar and execute the SQL script
               that you build along the way in a SQL Worksheet and see your creation in Snowflake!  Select a role and a warehouse in order to execute your script.\n
   Hint:  Warehouses double in resources with each size in Snowflake.  After establishing an initial size, then apply performance tuning practices on future executions.)
            \n
               """
         )
         display_snowflake_docs_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         inp_Q001_pre = ("explain \n" 
         "select c_name, c_mktsegment, o_totalprice, o_orderstatus \n"  
         "from snowflake_sample_data.tpch_sf10.customer c \n" 
         "join snowflake_sample_data.tpch_sf10.orders o \n" 
         "on c.c_custkey = o.o_custkey; \n"
         "-- bytes_assigned = .55 GB")
         
         inp_Q002_pre = ("explain \n" 
         "select c_name, c_mktsegment, o_totalprice, o_orderstatus \n"  
         "from snowflake_sample_data.tpch_sf100.customer c \n" 
         "join snowflake_sample_data.tpch_sf100.orders o \n" 
         "on c.c_custkey = o.o_custkey; \n"
         "-- bytes_scanned = 5.73 GB")
         
         inp_Q003_pre = ("explain \n" 
         "select c_name, c_mktsegment, o_totalprice, o_orderstatus \n"  
         "from snowflake_sample_data.tpch_sf1000.customer c \n" 
         "join snowflake_sample_data.tpch_sf1000.orders o \n" 
         "on c.c_custkey = o.o_custkey; \n"
         "-- bytes_scanned = 63.10 GB")
         
         inp_Q004_pre = ("explain \n" 
         "select c_mktsegment\n" 
         "    , sum(o_totalprice) as total_sales"
         "from snowflake_sample_data.tpch_sf1000.customer c \n" 
         "join snowflake_sample_data.tpch_sf1000.orders o \n" 
         "on c.c_custkey = o.o_custkey \n"
         "group by all; \n"
         "-- bytes_scanned = 63.09 GB")
         
         inp_Q005_pre = ("explain \n" 
         "select c_name, c_mktsegment, o_totalprice, o_orderstatus \n"  
         "from snowflake_sample_data.tpch_sf10.customer c \n" 
         "join snowflake_sample_data.tpch_sf10.orders o \n" 
         "on c.c_custkey = o.o_custkey \n"
         "where  o_orderdate >= '1997-08-02'; \n"
         "-- bytes_scanned = 18.84 GB")
         
         st.markdown('**Question 1:**  Consider the bytes_assigned that are returned on the GlobalStats row in the Explain plan results: \n')
         displaycode(inp_Q001_pre)
         
         inp_Q001 = st.selectbox(
               "*What warehouse size should you pick for this query?*",
               ['',
               'X-Small',
               'Small',
               'Medium',
               'Large']
         )
         
         if inp_Q001 != 'X-Small' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
               displaycode(inp_Q001)
               print("")
               st.markdown('**Question 2:**  Note that tpch_sf100 is a larger table: \n')
               displaycode(inp_Q002_pre)
         
               inp_Q002 = st.selectbox(
                  "*Would you select a different warehouse size for this query?*",
               ['',
               'X-Small',
               'Small',
               'Medium',
               'Large']
               )
         
               if inp_Q002 != "Large" and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
                  displaycode(inp_Q002)
                  print("")
                  st.markdown('**Question 3:**  Note that tpch_sf1000 is an even larger table: \n')
                  displaycode(inp_Q003_pre)
         
                  inp_Q003 = st.selectbox(
                     "*What warehouse size would work for this query?*",
                  ['',
                  'Large',
                  'X-Large',
                  '2X-Large',
                  '3X-Large']
                  )
               
                  if inp_Q003 != "3X-Large" and inp_Q003 != '':
                     displaytext_tryagain(CON_POINTS2)
                  elif inp_Q003 != '' or logic_override:
                     displaytext_correct(CON_POINTS3)
                     displaycode(inp_Q003)
                     print("")
                     st.markdown('**Question 4:**  What if you change the large table query to be an aggregation query: \n')
                     displaycode(inp_Q004_pre)
               
                     inp_Q004 = st.selectbox(
                           "*Can you use a smaller warehouse size?*",
                     ['',
                        'Large - there are only a few market segment rows as the output',
                        'X-Large - it scans less rows',
                        '2X-Large - it scans less rows, but there is a calculation',
                        '3X-Large - it still scans the same number of partitions and close to the same bytes']
                     )
         
                     if inp_Q004 != "3X-Large - it still scans the same number of partitions and close to the same bytes" and inp_Q004 != '':
                           displaytext_tryagain(CON_POINTS3)
                     elif inp_Q004 != '' or logic_override:
                           displaytext_correct(CON_POINTS4)
                           displaycode(inp_Q004)
                           print("")
                           st.markdown('**Question 5:**  What if you filter the large table aggregation query: \n')
                           displaycode(inp_Q005_pre)
                  
                           inp_Q005 = st.selectbox(
                              "*Now what warehouse size would you select?*",
                           ['',
                           'Large - the calculation is easier to process',
                           'X-Large - it scans less bytes and therefore less partitions',
                           '2X-Large - it still scans almost the same number of partitions and bytes',
                           '3X-Large - it still scans the same number of partitions']
                           )
            
                           if inp_Q005 != "X-Large - it scans less bytes and therefore less partitions" and inp_Q005 != '':
                              displaytext_tryagain(CON_POINTS4)
                           elif inp_Q005 != '' or logic_override:
                              displaytext_correct(CON_POINTS5)
                              displaycode(inp_Q005)
                              print("")
                              
                              ctr_Q002 = st.container()
                  
                              opts_Q006 = ctr_Q002.multiselect("**Under what conditions can you put the large table aggregation query on a smaller warehouse size?  Select two.**",
                                    ['There is no disk spill to local or remote storage.', 'The query calculation becomes very complex.', 'There is extremely high cache usage.','There is low to medium cache usage.'])
                  
                              if len(opts_Q006) == 0:
                                 st.write('')
                              elif len(opts_Q006) > 0 and len(opts_Q006) < 2:
                                 st.write(':green[*Select all items in proper sequence for score*]')
                              elif len(opts_Q006) > 2 :
                                 st.write(':green[*You have selected too many items*]')
                              elif len(opts_Q006) == 2:
                                 if opts_Q006[0] != 'There is no disk spill to local or remote storage.' \
                                 and opts_Q006[3] != 'There is low to medium cache usage.':
                                       displaytext_tryagain(CON_POINTS5)
                                 else:
                                       displaytext_correct(CON_POINTS6)
                                       displaycode(opts_Q006[0] + " \n" + opts_Q006[1])
         
                              displaytext_pass_game()
                              st.markdown(":blue[Run each of the following EXPLAIN statements one at a time in a SQL Worksheet to see their query plan output.]")
                              displaycode(inp_Q001_pre + " \n\n" + inp_Q002_pre + " \n\n" + inp_Q003_pre + " \n\n" + inp_Q004_pre + " \n\n" + inp_Q005_pre) 
                              st.session_state.con_sql_lvl1_warehousesizing = CON_POINTS6
                              displaytext_total_game_points()
                              displaytext_pass_level()

   #--------------------------------------------------------------------
   # con_sql_lvl2_dynamictables #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl2_dynamictables':
      
         st.subheader(":blue[SQL Level 2 - Create a Dynamic Table]")
         st.markdown(
               """
               Each correct answer builds your SQL script and your score!  At the end, click the Worksheets button from the left navigation bar and execute the SQL script
               that you build along the way in a SQL Worksheet and see your creation in Snowflake!  Select a role and a warehouse in order to execute your script. \n
               """
         )
         st.markdown("""*:blue[This game depends on the preliminary scripts to be ran first:]*""")
         st.markdown("*:blue[Level 1 - Database Setup&nbsp;&nbsp; -- &nbsp;&nbsp;Level 1 - SQL Joins and Views]*")  
         display_snowflake_dynamic_tables_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         out_Q003_answer = "'1 minute', '1 day', '15 minutes'"
         
         inp_Q004_pre = ("create dynamic table product_metrics_dt \n"  
         "target_lag = '1 minute' \n" 
         "warehouse = compute_wh \n" 
         "as \n"
         "select product_type_name, product_count, product_amount, metric_date \n"
         "from fact_metrics f \n"
         "inner join dim_product_types p \n"
         "on f.product_type_id = p.product_type_id;")
         
         inp_Q005a_post = ("\n" 
         "use database analytics; \n"
         "use schema metrics;")
         
         inp_Q005b_post = ("\n" 
         "select * from product_metrics_dt;")
         
         inp_Q001 = st.selectbox(
               '**What best describes a dynamic table?**',
               ['',
               'The create table syntax is a set of dynamic string values',
               'Underlying it is a permanent table with a custom definition',
               'The table is populated with values that are dynamically generated on the fly']
         )
         
         if inp_Q001 != 'Underlying it is a permanent table with a custom definition' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
         
               inp_Q002 = st.selectbox(
                  "**The custom definition of a dynamic table is similar to a view?**",
               ['',
               'False',
               'True']
               )
         
               if inp_Q002 != "True" and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
         
                  ctr_Q001 = st.container()
               
                  opts_Q003 = ctr_Q001.multiselect("**What are valid intervals for a dynamic table to be refreshed?**   *Check all that apply.*",
                        ['1 minute','15 minutes','1 day', 'ONDEMAND'])
               
                  if len(opts_Q003) == 0:
                     st.write('')
                  elif len(opts_Q003) > 0 and len(opts_Q003) < 3:
                     st.write(':green[*Select all items that apply for the score*]')
                  elif len(opts_Q003) > 3 :
                     st.write(':green[*You have selected too many items.  Try again.*]')
                  elif len(opts_Q003) == 3:
                     if opts_Q003[0] in out_Q003_answer \
                     and opts_Q003[1] in out_Q003_answer \
                     and opts_Q003[2] in out_Q003_answer:
                           displaytext_correct(CON_POINTS3)
                     else:
                           displaytext_tryagain(CON_POINTS2)
                  
                     inp_Q004 = st.selectbox(
                           "**What size warehouse does a dynamic table need by default?**",
                     ['',
                        'It does not need a warehouse, because it is a metadata statement.',
                        'It needs a warehouse large enough to process the data in the definition.']
                     )
                  
                     if inp_Q004 != "It needs a warehouse large enough to process the data in the definition." and inp_Q004 != '':
                           displaytext_tryagain(CON_POINTS2)
                     elif inp_Q004 != '' or logic_override:
                           displaytext_correct(CON_POINTS3)
                           print("")
                           st.markdown('**Question 4:** Consider the following create statement for a dynamic table: \n')
                           displaycode(inp_Q004_pre)
                  
                           inp_Q004 = st.selectbox(
                              "**What is wrong with the syntax?**",
                           ['',
                           'The "target_lag" property should be "interval"',
                           'The "warehouse" property should be "target_warehouse"',
                           'The "as" keyword should be before the properties instead of after',
                           'None of the above']
                           )
               
                           if inp_Q004 != "None of the above" and inp_Q004 != '':
                              displaytext_tryagain(CON_POINTS3)
                           elif inp_Q004 != '' or logic_override:
                              displaytext_correct(CON_POINTS4)
                              displaycode(inp_Q004)
                                          
                              ctr_Q002 = st.container()
                  
                              opts_Q005 = ctr_Q002.multiselect("**What statement will cause new data to display the next time the dynamic table is refreshed after the interval?**  *Choose all that apply.*",
                              ['insert into dim_product_types values(4,' + "'" + 'car' + "'" + ');', 'insert into fact_metrics values(4, 1, ' + "'" + '2024-08-27' + "'" + ',4,3691);', 'update fact_metrics set product_count = 242 where metric_id = 1;','delete from fact_metrics where metric_id = 2;'])
               
                              if len(opts_Q005) == 0:
                                 st.write('')
                              elif len(opts_Q005) > 0 and len(opts_Q005) < 4:
                                 st.write(':green[*Select all items that apply*]')
                                 displaytext_tryagain(CON_POINTS4)
                              elif len(opts_Q005) == 4:
                                 displaytext_correct(CON_POINTS5)
                  
                                 displaytext_pass_game()
                                 st.markdown(":blue[Execute the following dynamic table statement in a SQL Worksheet, query the table, then modify the data.  Wait 1 minute and query the table again.]")
                                 displaycode(inp_Q005a_post + " \n\n" +inp_Q004_pre + " \n" +  inp_Q005b_post + " \n\n" + opts_Q005[1] + " \n" + inp_Q005b_post) 
                                 st.session_state.con_sql_lvl2_dynamictables = CON_POINTS5
                                 displaytext_total_game_points()
         
   #--------------------------------------------------------------------
   # con_sql_lvl2_dynamictablesnext #

   with st.container():
      if st.session_state.active_game_name == 'con_sql_lvl2_dynamictablesnext':

         st.subheader(":blue[SQL Level 2 - Dynamic Tables next steps]")
         st.markdown(
               """
               Each correct answer builds your SQL script and your score!  At the end, click the Worksheets button from the left navigation bar and execute the SQL script
               that you build along the way in a SQL Worksheet and see your creation in Snowflake!  Select a role and a warehouse in order to execute your script. \n
               """
         )
         st.markdown("""*:blue[This game depends on the preliminary scripts to be ran first:]*""")
         st.markdown("*:blue[Level 1 - Database Setup&nbsp;&nbsp; -- &nbsp;&nbsp;Level 1 - SQL Joins and Views&nbsp;&nbsp; -- &nbsp;&nbsp;Level 2 - Create a Dynamic Table]*")  
      
         display_snowflake_dynamic_tables_next_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         out_Q003_answer = "'Dynamic tables incur compute costs upon their scheduled interval even if they process no underlying changes', 'Dynamic tables have a full or incremental refresh mode'"
         
         out_Q004_answer = "'NO_DATA | INCREMENTAL','CREATION | SCHEDULED'"
         
         inp_Q004_pre = ("select name, schema_name, database_name, state_code, state_message, query_id \n"  
         "    , data_timestamp, refresh_start_time, refresh_end_time \n" 
         "    , datediff(milliseconds,refresh_start_time, refresh_end_time) as refresh_duration_ms \n" 
         "    , refresh_action, refresh_trigger \n"
         "from table(analytics.information_schema.dynamic_table_refresh_history()) \n"
         "order by name, data_timestamp desc;")
         
         inp_Q005a_post = ("\n" 
         "use database analytics; \n"
         "use schema metrics;")
         
         inp_Q005b_post = ("\n" 
         "select * from product_metrics_dt;")
         
         inp_Q001 = st.selectbox(
               '**Which of the following are true about dynamic tables?** *Check all that apply.*',
               ['',
               'The dynamic table definition query can contain user-defined functions',
               'The dynamic table definition query can contain dynamic SQL',
               'Tables being queried must have CDC (Change Data Capture) enabled on them']
         )
         
         if inp_Q001 != 'Tables being queried must have CDC (Change Data Capture) enabled on them' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
         
               inp_Q002 = st.selectbox(
                  "**Can a dynamic table query another dynamic query in its custom definition?**",
               ['',
               'False',
               'True']
               )
         
               if inp_Q002 != "True" and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
         
                  ctr_Q001 = st.container()
               
                  opts_Q003 = ctr_Q001.multiselect("**Select the following statements that are true:**   *Check all that apply.*",
                        ['Dynamic tables incur compute costs upon their scheduled interval even if they process no underlying changes','Materialized views have the same functionality as dynamic tables', 'Dynamic tables have a full or incremental refresh mode'])
               
                  if len(opts_Q003) == 0:
                     st.write('')
                  elif len(opts_Q003) > 0 and len(opts_Q003) < 2:
                     st.write(':green[*Select all items that apply for the score*]')
                  elif len(opts_Q003) > 2 :
                     st.write(':green[*You have selected too many items.  Try again.*]')
                  elif len(opts_Q003) == 2:
                     if opts_Q003[0] not in out_Q003_answer \
                     and opts_Q003[1] not in out_Q003_answer:
                           st.markdown(opts_Q003)
                           displaytext_tryagain(CON_POINTS2)
                     else:
                           displaytext_correct(CON_POINTS3)        
                           print("")
                           st.markdown('**Question 4:**Execute the following statement in the SQL Worksheet: \n')
                           displaycode(inp_Q004_pre)                    
                                    
                           ctr_Q002 = st.container()
               
                           opts_Q004 = ctr_Q002.multiselect("**Which of the following combination of values can you see in the refresh_action and refresh_trigger columns?**  *Choose all that apply.*",
                              ['NO_DATA | SCHEDULED', 'NO_DATA | CREATION', 'NO_DATA | INCREMENTAL','CREATION | SCHEDULED'])
         
                           if len(opts_Q004) == 0:
                              st.write('')
                           elif len(opts_Q004) > 0 and len(opts_Q004) < 2:
                              st.write(':green[*Select all items that apply*]')
                              displaytext_tryagain(CON_POINTS3)
                           elif len(opts_Q004) > 2 :
                              st.write(':green[*You have selected too many items.  Try again.*]')
                              displaytext_tryagain(CON_POINTS3)
                           elif len(opts_Q004) == 2 and 'NO_DATA | SCHEDULED' in opts_Q004 and 'NO_DATA | CREATION' in opts_Q004:  
                              displaytext_correct(CON_POINTS4)
                              displaytext_pass_game()
                              displaytext_pass_level()
                              st.session_state.con_sql_lvl2_dynamictablesnext = CON_POINTS4
                              displaytext_total_game_points()

   #--------------------------------------------------------------------
   # con_inter_warehousesizing_1 #

   with st.container():
      if st.session_state.active_game_name == 'con_inter_warehousesizing_1':

         st.subheader(":blue[Puzzles - Intermediate - Warehouse Sizing Challenge - #1]")
         st.markdown("""Each correct answer builds your score!""")
         st.markdown("""*:blue[This game depends on the preliminary scripts to be ran first:]*""")
         st.markdown("*:blue[Level 1 - Database Setup&nbsp;&nbsp; -- &nbsp;&nbsp;Level 1 - SQL Joins and Views&nbsp;&nbsp; -- &nbsp;&nbsp;Level 2 - Create a Dynamic Table]*") 

         display_snowflake_docs_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         out_Q001_answer = "'It should not take 7 mins to retrieve 15 GB of data, so it should be on a larger warehouse', 'It should be ran on a different schedule to avoid blocking.'"
         
         inp_Q001_pre = ("bytes_scanned:                      15.46 GB \n"  
         "partitions_scanned:                 1022 \n" 
         "total_partitions:                   1022 \n" 
         "bytes_scanned_from_local_storage:   0 GB \n" 
         "bytes_scanned_from_remote_storage:  0 GB \n" 
         "percent_scanned_from_cache:         30% \n" 
         "transaction_blocked_time:           247 ms\n"
         "queued_overload_time:               0 ms \n"
         "warehouse_size:                     X-Small \n"
         "total_elapsed_time:                 7.764500  (minutes) \n"
         "credits_used_cloud_service:         0.000034")
         
         inp_Q002_pre = ("bytes_scanned:                      15.46 GB \n"  
         "partitions_scanned:                 1022 \n" 
         "total_partitions:                   1022 \n" 
         "bytes_scanned_from_local_storage:   0 GB \n" 
         "bytes_scanned_from_remote_storage:  0 GB \n" 
         "percent_scanned_from_cache:         30% \n" 
         "transaction_blocked_time:           0 ms\n"
         "queued_overload_time:               0 ms \n"
         "warehouse_size:                     Medium \n"
         "total_elapsed_time:                 2.047567  (minutes) \n"
         "credits_used_cloud_service:         0.000035")
         
         inp_Q003_pre = ("bytes_scanned:                      201.53 GB \n"  
         "partitions_scanned:                 13730 \n" 
         "total_partitions:                   13720 \n" 
         "bytes_scanned_from_local_storage:   154 GB \n" 
         "bytes_scanned_from_remote_storage:  0 GB \n" 
         "percent_scanned_from_cache:         60% \n" 
         "transaction_blocked_time:           0 ms\n"
         "queued_overload_time:               0 ms \n"
         "warehouse_size:                     Medium \n"
         "total_elapsed_time:                 98.78922  (minutes) \n"
         "credits_used_cloud_service:         0.000470")
         
         inp_Q004_pre = ("bytes_scanned:                      201.53 GB \n"  
         "partitions_scanned:                 13730 \n" 
         "total_partitions:                   13720 \n" 
         "bytes_scanned_from_local_storage:   40 GB \n" 
         "bytes_scanned_from_remote_storage:  0 GB \n" 
         "percent_scanned_from_cache:         10% \n" 
         "transaction_blocked_time:           0 ms\n"
         "queued_overload_time:               0 ms \n"
         "warehouse_size:                     3X-Large \n"
         "total_elapsed_time:                 6.170000  (minutes) \n"
         "credits_used_cloud_service:         0.000464")
         
         
         inp_Q005b_post = ("\n" 
         "select * from snowflake.account_usage.query_history;")
         
         st.markdown('**Question 1:**  Consider the following query statistics: \n')
         displaycode(inp_Q001_pre)
         
         ctr_Q001 = st.container()
                  
         opts_Q001 = ctr_Q001.multiselect('**Is this query on the right warehouse size?** *Check all reasons that apply.*',
               ['Partitions scanned equal Total Partitions, so it should be on a larger warehouse',
               'The query should utilize more cache, so it should be on a smaller warehouse',
               'It should not take 7 mins to retrieve 15 GB of data, so it should be on a larger warehouse',
               'It should be ran on a different schedule to avoid blocking.']
         )
         
         if len(opts_Q001) == 0:
               st.write('')
         elif len(opts_Q001) > 0 and len(opts_Q001) < 2:
               st.write(':green[*Select all items that apply for the score*]')
         elif len(opts_Q001) > 2 :
               st.write(':green[*You have selected too many items.  Try again.*]')
         elif len(opts_Q001) == 2:
               st.markdown(opts_Q001)
               if opts_Q001[0] not in out_Q001_answer \
               and opts_Q001[1] not in out_Q001_answer:
                  displaytext_tryagain(CON_POINTS0)
               else:
                  displaytext_correct(CON_POINTS1)        
                  print("")
                  st.markdown('**Question 2:**  The same query from Question #1 was executed on a Medium warehouse with these statistics: \n')
                  displaycode(inp_Q002_pre)
               
                  inp_Q002 = st.selectbox(
                     "**Why is the cost the same when there are 4x more resources on a Medium than a X-Small?**",
                  ['',
                  'In Snowflake, each warehouse size larger is 2x more cost and approximately 2x faster',
                  'In Snowflake, warehouses all cost the same']
                  )
               
                  if inp_Q002 != "In Snowflake, each warehouse size larger is 2x more cost and approximately 2x faster" and inp_Q002 != '':
                     displaytext_tryagain(CON_POINTS1)
                  elif inp_Q002 != '' or logic_override:
                     displaytext_correct(CON_POINTS2)
                     st.markdown("")
                     st.markdown('**Question 3:**  The same query from Question #2 was executed on a Medium warehouse on a larger table with these statistics: \n')
                     displaycode(inp_Q003_pre)
               
                     ctr_Q002 = st.container()
                  
                     inp_Q003 = ctr_Q002.selectbox("**Why is this query more expensive?**   *Check all that apply.*",
                           ['',
                           'It made better use of cache',
                           'It is scanning too much data for this size and is spilling to the local SSD which incurs I/O', 
                           'The Partitions Scanned still equals Total Partitions'])
                  
                     if inp_Q003 != "It is scanning too much data for this size and is spilling to the local SSD which incurs I/O" and inp_Q002 != '':
                           displaytext_tryagain(CON_POINTS3)
                     elif inp_Q003 != '' or logic_override:
                           displaytext_correct(CON_POINTS4)
                           print("")
                           st.markdown('**Question 4:**  The same larger table query from Question #3 was executed on a 3X-Large warehouse with these statistics: \n')
                           displaycode(inp_Q004_pre)                    
                                    
                           ctr_Q002 = st.container()
                  
                           opts_Q004 = ctr_Q002.multiselect("**Why is the cost 1% cheaper?**  *Choose all that apply.*",
                              ['Because it used less cache', 'It still spilled to local disk, so it should not be cheaper', 'Because it was faster','Because it used larger resources more effectively and with less spill'])
                  
                           if len(opts_Q004) == 0:
                              st.write('')
                           elif len(opts_Q004) > 2:
                              st.write(':green[*You have selected too many items.  Try again.*]')  
                           elif len(opts_Q004) == 1 and opts_Q004[0] == 'Because it used larger resources more effectively and with less spill':
                              displaytext_correct(CON_POINTS4)
                              displaytext_pass_game()
                           else:
                              displaytext_tryagain(CON_POINTS5)        
                              st.session_state.con_inter_warehousesizing_1 = CON_POINTS5
                              displaytext_total_game_points()
                  

   #--------------------------------------------------------------------
   # con_inter_queryoptimizing_2 #

   with st.container():
      if st.session_state.active_game_name == 'con_inter_queryoptimizing_1':

         st.subheader(":blue[Puzzles - Intermediate - Optimizing Queries #1]")
         st.markdown(
               """
               Each correct answer builds your score! \n
               \n
               """
         )
         display_snowflake_docs_url()
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         # This will show all questions and their answers when set to True
         logic_override = False;
         
         out_Q001_answer = "'Change the join order sequence to be most restrictive table first:  customer, orders, lineitem, part', 'Change the order of columns in join clauses to be most restive table first'"
         out_Q003_answer = "'It can overload the resources if put on too small of a warehouse','It is scanning the largest table, lineitem, too many times, so break into three separate queries'"
         out_Q004_answer = "'NO_DATA | INCREMENTAL','CREATION | SCHEDULED'"
         
         inp_Q001_pre = ("select c_name \n"  
         "    , c_mktsegment \n" 
         "    , p_type \n" 
         "    , sum(o_totalprice) as total_price \n" 
         "from snowflake_sample_data.tpch_sf1.lineitem li \n" 
         "join snowflake_sample_data.tpch_sf1.part p \n" 
         "on li.l_partkey = p.p_partkey \n"
         "join snowflake_sample_data.tpch_sf1.orders o \n"
         "on o.o_orderkey = li.l_orderkey \n"
         "join snowflake_sample_data.tpch_sf1.customer c \n"
         "on o.o_custKey = c.c_custkey \n"
         "group by all;")
         
         inp_Q002_pre = ("select c_name \n"  
         "    , c_mktsegment \n" 
         "    , p_type \n" 
         "    , sum(o_totalprice) as total_price \n" 
         "from snowflake_sample_data.tpch_sf1.customer c \n" 
         "join snowflake_sample_data.tpch_sf1.orders o \n"
         "on c.c_custkey = o.o_custKey \n"
         "join snowflake_sample_data.tpch_sf1.lineitem li \n"
         "on o.o_orderkey = li.l_orderkey \n"
         "join snowflake_sample_data.tpch_sf1.part p \n" 
         "on li.l_partkey = p.p_partkey \n"
         "group by all;")
         
         inp_Q003_pre = ("with main_orders as ( \n"
         "select c_name \n"  
         "    , c_mktsegment \n" 
         "    , p_type \n" 
         "    , sum(l_quantity) as total_quantity \n"
         "    , sum(o_totalprice) as total_price \n" 
         "    , max(l_shipdate) as most_recent_shipdate \n" 
         "from snowflake_sample_data.tpch_sf1.customer c \n" 
         "join snowflake_sample_data.tpch_sf1.orders o \n"
         "on c.c_custkey = o.o_custKey \n"
         "join snowflake_sample_data.tpch_sf1.lineitem li \n"
         "on o.o_orderkey = li.l_orderkey \n"
         "join snowflake_sample_data.tpch_sf1.part p \n" 
         "on li.l_partkey = p.p_partkey \n"
         "group by all \n"
         "),"
         "shipdate_details as ( \n"
         "select l_shipdate \n"
         "	, count(*) as shipdate_count \n"
         "from snowflake_sample_data.tpch_sf1.lineitem li \n"
         "group by all \n"
         ") \n"
         "select c_name \n"  
         "    , c_mktsegment \n" 
         "    , p_type \n" 
         "    , total_price \n" 
         "    , most_recent_shipdate \n"
         "    , total_quantity / shipdate_count  as pct_total_quantity \n"
         "from main_orders mo \n" 
         "left join shipdate_details sd \n" 
         "on mo.most_recent_shipdate = sd.l_shipdate;")
         
         st.markdown('**Scenario 1:**  Consider the following query syntax: \n')
         displaycode(inp_Q001_pre)
         
         ctr_Q001 = st.container()
                  
         opts_Q001 = ctr_Q001.multiselect('**What can we do to optimize this query?** *Check all reasons that apply.*',
               ['',
               'List column names specifically in the group by clause',
               'Use left joins instead of inner joins',
               'Change the join order sequence to be most restrictive table first:  customer, part, orders, lineitem',
               'Change the order of columns in join clauses to be most restive table first']
         )
         
         if len(opts_Q001) == 0:
               st.write('')
         elif len(opts_Q001) > 0 and len(opts_Q001) < 2:
               st.write(':green[*Select all items that apply for the score*]')
         elif len(opts_Q001) > 2 :
               st.write(':green[*You have selected too many items.  Try again.*]')
         elif len(opts_Q001) == 2:
               if opts_Q001[0] not in out_Q001_answer \
               and opts_Q001[1] not in out_Q001_answer:
                  displaytext_tryagain(CON_POINTS0)
               else:
                  displaytext_correct(CON_POINTS1)        
                  print("")
                  st.markdown('**Scenario 2:**  The underlying data stores 10 years of data totalling 1 TB: \n')
                  displaycode(inp_Q002_pre)
               
                  inp_Q002 = st.selectbox(
                     "**What would be the best way to optimize this query?**",
                  ['',
                  'Remove Customer Name to aggregate the data to a higher grain',
                  'Filter the data to just look at the last 2 years',
                  'Pre-aggregate prior year data in a separate dynamic table so it only scans the last 90 days for the current aggregate amounts']
                  )
               
                  if inp_Q002 != "Pre-aggregate prior year data in a separate dynamic table so it only scans the last 90 days for the current aggregate amounts" and inp_Q002 != '':
                     displaytext_tryagain(CON_POINTS1)
                  elif inp_Q002 != '' or logic_override:
                     displaytext_correct(CON_POINTS2)
                     st.markdown("")
                     st.markdown('**Scenario 3:**  The following query has large data volumes: \n')
                     displaycode(inp_Q003_pre)
               
                     ctr_Q002 = st.container()
                  
                     opts_Q003 = ctr_Q002.multiselect("**What is the main issue that needs to be optimized with this query?**   *Check all that apply.*",
                           ['',
                           'It can overload the resources if put on too small of a warehouse',
                           'It is scanning the largest table (lineitem) too many times, so break into three separate queries', 
                           'There are no issues, because the first CTE (Common Table Expression) section puts all the data into local memory for the subsequent scans'])
                  
                     if len(opts_Q003) == 0:
                           st.write('')
                     elif len(opts_Q003) > 0 and len(opts_Q003) < 2:
                           st.write(':green[*Select all items that apply for the score*]')
                     elif len(opts_Q003) > 2 :
                           st.write(':green[*You have selected too many items.  Try again.*]')
                     elif len(opts_Q003) == 2:
                           if opts_Q003[0] not in out_Q003_answer \
                           and opts_Q003[1] not in out_Q003_answer:
                              displaytext_tryagain(CON_POINTS3)
                           else:
                              displaytext_correct(CON_POINTS4)        
         
                           inp_Q004 = st.selectbox(
                              "**What is the most efficient action to take to determine if the CTE in Scenario #3 needs to be put into separate queries?**",
                              ['',
                              'Run each CTE section separately and look at query statistics',
                              'Run the query with Explain before the syntax to see how many times tables are scanned, what the table scan sizes are, and which are the largest operators',
                              'Execute the query to try a variety of filters on the first CTE section to reduce data volumes']
                              )
                     
                           if inp_Q004 != "Run the query with Explain before the syntax to see how many times tables are scanned, what the table scan sizes are, and which are the largest operators" and inp_Q004 != '':
                              displaytext_tryagain(CON_POINTS4)					
                           elif inp_Q004 != '' or logic_override:
                              displaytext_correct(CON_POINTS5)
                              displaytext_pass_game()
                              st.session_state.con_inter_warehousesizing_1 = CON_POINTS5
                              displaytext_total_game_points()


   #--------------------------------------------------------------------
   # con_inter_dynamictable_1 #

   with st.container():
      if st.session_state.active_game_name == 'con_inter_dynamictable_1':

         st.subheader(":blue[Puzzles - Intermediate - Design a Dynamic Table #1]")
         st.markdown(
               """
               Design one or more Dynamic Tables using the query provided. \n
               \n
               Each correct answer builds your SQL script and your score!  Extra points may be awarded for insights that excel beyond expectations!
               """
         )
         st.markdown("""*Snowflake documentation - Dynamic Tables - Create - https://docs.snowflake.com/en/sql-reference/sql/create-dynamic-table*""")
         st.markdown("""*Snowflake documentation - Dynamic Tables - When to Use - https://docs.snowflake.com/en/user-guide/dynamic-tables-about*""")
         st.markdown("""*Snowflake documentation - Dynamic Tables Known Limitations - https://docs.snowflake.com/en/user-guide/dynamic-tables-limitations*""")
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         
         inp_Q001_pre = ("use schema snowflake_sample_data.tpcds_sf10Tcl; \n" 
         "with v1 as ( \n"
         "  select i_category, i_brand, cc_name, d_year, d_moy, \n" 
         "        sum(cs_sales_price) sum_sales, \n" 
         "        avg(sum(cs_sales_price)) over \n" 
         "          (partition by i_category, i_brand, \n" 
         "                     cc_name, d_year) \n" 
         "          avg_monthly_sales, \n" 
         "        rank() over \n" 
         "          (partition by i_category, i_brand, \n" 
         "                     cc_name \n" 
         "           order by d_year, d_moy) rn \n" 
         "  from item, catalog_sales, date_dim, call_center \n" 
         "  where cs_item_sk = i_item_sk and \n" 
         "       cs_sold_date_sk = d_date_sk and \n" 
         "       cc_call_center_sk= cs_call_center_sk and \n" 
         "       ( \n" 
         "         d_year = 1999 or \n" 
         "         ( d_year = 1999-1 and d_moy =12) or \n" 
         "         ( d_year = 1999+1 and d_moy =1) \n" 
         "       ) \n" 
         "  group by i_category, i_brand, \n" 
         "          cc_name , d_year, d_moy), \n" 
         "v2 as( \n" 
         "  select v1.i_category ,v1.d_year, v1.d_moy ,v1.avg_monthly_sales \n" 
         "        ,v1.sum_sales, v1_lag.sum_sales psum, v1_lead.sum_sales nsum \n" 
         "  from v1, v1 v1_lag, v1 v1_lead \n" 
         "  where v1.i_category = v1_lag.i_category and \n" 
         "       v1.i_category = v1_lead.i_category and \n" 
         "       v1.i_brand = v1_lag.i_brand and \n" 
         "       v1.i_brand = v1_lead.i_brand and \n" 
         "       v1.cc_name = v1_lag.cc_name and \n" 
         "       v1.cc_name = v1_lead.cc_name and \n" 
         "       v1.rn = v1_lag.rn + 1 and \n" 
         "       v1.rn = v1_lead.rn - 1) \n" 
         "select  * \n" 
         "from v2 \n" 
         "where  d_year = 1999 and \n" 
         "        avg_monthly_sales > 0 and \n" 
         "        case when avg_monthly_sales > 0 then abs(sum_sales - avg_monthly_sales) / avg_monthly_sales else null end > 0.1 \n" 
         "order by sum_sales - avg_monthly_sales, 3; \n\n" 
         "-- use limit 100; if executing to see data results \n" 
         "")
         
         st.markdown('Consider the following CTE (Common Table Expression): \n')
         displaycode(inp_Q001_pre)
         display_blank_line()
         display_blank_line()
                  
         st.markdown("""**Question 1:  Would you make a Dynamic Table of the entire CTE or break up the sub section queries into their own Dynamic Tables,
         then query those Dynamic Tables from this main query?**
         \n\n
         Create the solution in a SQL Worksheet that you would implement and show the event coordinator to be awarded points. \n
         *Hint:  use Explain to check the sections versus the total query.*'
         """)
         
         st.markdown("""**12 Points Possible:** \n
               Create Dynamic Table - 2 points \n
               Select correct warehouse size - 2 points (2 additional possible) \n
               Use of Explain - 2 points \n
               Identify dynamic table limitations - 2 points \n
               Solve dynamic table limitations through optimization - 4 points """
         )
         display_blank_line()
         
         st.markdown('Show script to event coordinator when done.')


   #--------------------------------------------------------------------
   # con_inter_dynamictable_2 #

   with st.container():
      if st.session_state.active_game_name == 'con_inter_dynamictable_2':

         st.subheader(":blue[Puzzles - Intermediate - Design a Dynamic Table #2]")
         st.markdown(
               """
               Review and solve the Dynamic Table limitation. \n
               \n
               4 points possible!
               """
         )
         st.markdown("""*Snowflake documentation - Dynamic Tables - Create - https://docs.snowflake.com/en/sql-reference/sql/create-dynamic-table*""")
         st.markdown("""*Snowflake documentation - Dynamic Tables - When to Use - https://docs.snowflake.com/en/user-guide/dynamic-tables-about*""")
         st.markdown("""*Snowflake documentation - Dynamic Tables Known Limitations - https://docs.snowflake.com/en/user-guide/dynamic-tables-limitations*""")
         st.markdown("""---""")
         
         # Get the current credentials
         session = get_active_session()
         
         
         inp_Q001_pre = ("use schema snowflake_sample_data.tpch_sf1000; \n"  
         "  select \n" 
         "        l_returnflag, \n" 
         "        l_linestatus, \n" 
         "        sum(l_quantity) as sum_qty, \n" 
         "       sum(l_extendedprice) as sum_base_price, \n" 
         "       sum(l_extendedprice * (1-l_discount)) as sum_disc_price,  \n" 
         "        sum(l_extendedprice * (1-l_discount) * (1+l_tax)) as sum_charge, \n" 
         "       avg(l_quantity) as avg_qty,  \n" 
         "       avg(l_extendedprice) as avg_price,  \n" 
         "       avg(l_discount) as avg_disc,  \n" 
         "       count(*) as count_order  \n" 
         "from  \n" 
         "       lineitem  \n" 
         "where  \n" 
         "       l_shipdate <= dateadd(day, -90, to_date('1998-12-01'))  \n" 
         "group by  \n" 
         "       l_returnflag,  \n" 
         "       l_linestatus  \n" 
         "order by  \n" 
         "       l_returnflag,  \n" 
         "       l_linestatus;  \n" 
         "-- use limit 10; if executing to see data results \n" 
         "")
         
         st.markdown('Consider the following CTE (Common Table Expression): \n')
         displaycode(inp_Q001_pre)
         display_blank_line()
         display_blank_line()
                  
         st.markdown("""**Question 1: How would you solve the limitation that exists in this query to put this into a Dynamic Table?**  \n\n
         Create the solution in a SQL Worksheet that you would implement.  Total 4 possible points. \n\n
         *Hint:  use Explain on the query to help identify areas for possible improvement.*""")
         
         st.markdown("""**Points:** \n
               Solve limitation - 2 points \n
               Cost evaluation - 2 points """
         )
         display_blank_line()
         
         st.markdown('Discuss with event coordinator when done.')



   #--------------------------------------------------------------------
   # con_adv_streamlitgame_1 #

   with st.container():
      if st.session_state.active_game_name == 'con_adv_streamlitgame_1':

         st.subheader(":blue[Streamlit - Advanced - Create a Question Game]")
         st.markdown(
               """
               Modify the existing Streamlit app code to ask your own set of questions!  At the end, establish a runnable SQL script
               from the answers that can be executed in a SQL Worksheet and see your creation in Snowflake!  \n
            You get 10 points for a 4-question game!
               """
         )
         display_snowflake_docs_url()
         
         st.markdown("""
         1. Go to Streamlit on the left navigation bar.
         \n2. Click "+ Streamlit App" button in upper right corner.
         \n3. Provide a name for your Game and click Create on the popup.
         \n3. Click Edit button in upper right corner.
         \n4. Paste the following code in the left panel.
         \n5. Modify questions and answers.
         \n6. Click RUN after each change to test your code.
         \n\n **COPY CODE BELOW HERE**:
         """)

         st.code("""
         import streamlit as st
         from snowflake.snowpark.context import get_active_session
         
         st.set_page_config(layout="wide")
         st.session_state.total_points = 0
         
         CON_POINTS0 = 0
         CON_POINTS1 = 1
         CON_POINTS2 = 2
         CON_POINTS3 = 3
         CON_POINTS4 = 4
         
         def displaytext_correct(score):
               st.markdown(f':green[Correct!  (score={score})]')
         
         def displaytext_tryagain(score):
               st.markdown(f':red[Try again  (score={score})]')
         
         def displaycode(syntax_text):
               st.code(syntax_text, language="SQL")
         
         def displaytext_pass_game():
               st.markdown(f':blue[CONGRATULATIONS! YOU WON THIS GAME!]')
         
         def display_blank_line():
               st.markdown(" ")
         
         st.title(":blue[Snowflake Games]")
         
         session = get_active_session()
         
         # change this to False to run game one question at a time after debugging
         logic_override = True;
         
         inp_Q001 = st.selectbox(
         'Which statement will add a new database named "analytics" to Snowflake?',
         ['',
            'database.add = "analytics";',
            'create database = "analytics";',
            'create database analytics;']
         )
         
         if inp_Q001 != 'create database analytics;' and inp_Q001 != '':
               displaytext_tryagain(CON_POINTS0)
         elif inp_Q001 != '' or logic_override:
               displaytext_correct(CON_POINTS1)
               displaycode(inp_Q001)
               
               inp_Q002 = st.selectbox(
                  '**Which statement will add a new schema named "metrics"?**',
                  ['',
                  'create schema as metrics;',
                  'create schema metrics;',
                  'analytics.add = "metrics";']
               )
               
               if inp_Q002 != 'create schema metrics;' and inp_Q002 != '':
                  displaytext_tryagain(CON_POINTS1)
               elif inp_Q002 != '' or logic_override:
                  displaytext_correct(CON_POINTS2)
                  displaycode(inp_Q002)
               
                  inp_Q003 = st.selectbox(
                     '**Which statement activates a database or schema to be the current context that commands will execute in?**',
                     ['',
                        'use schema = metrics;',
                        'use metrics;',
                        'use schema metrics;']
                  )
               
                  if inp_Q003 != 'use schema metrics;' and inp_Q003 != '':
                     displaytext_tryagain(CON_POINTS2)
                  elif inp_Q003 != '' or logic_override:
                     displaytext_correct(CON_POINTS3)
                     displaycode(inp_Q003)
               
                     ctr_Q002 = st.container()
               
                     opts_Q004 = ctr_Q002.multiselect("**Select the commands to establish a database and schema and activate them in the order they need to be executed.  Use all selections.**",
                           ['create schema metrics;', 'use database analytics;', 'create database analytics;','use schema metrics;'])
               
                     if len(opts_Q004) == 0:
                           st.write('')
                     elif len(opts_Q004) > 0 and len(opts_Q004) < 4:
                           st.write(':green[*Select all items in proper sequence for score*]')
                     elif len(opts_Q004) == 4:
                           if opts_Q004[0] != 'create database analytics;' \
                           or opts_Q004[1] != 'use database analytics;'\
                           or opts_Q004[2] != 'create schema metrics;'\
                           or opts_Q004[3] != 'use schema metrics;':
                              displaytext_tryagain(CON_POINTS3)
                           else:
                              displaytext_correct(CON_POINTS4)
                              displaytext_pass_level()
                              st.markdown(f':blue[Execute the following script in a SQL Worksheet as sysadmin to create a database with your custom schema.  Use the sysadmin role for all your scripts.  Refresh the object explorer when done to see the database and schema.]')
                              displaycode(opts_Q004[0] + " " + opts_Q004[1] + " " + opts_Q004[2] + " " + opts_Q004[3])
                  """)

         st.markdown('*:blue[Show to event coordinator when done.]*')

if __name__ == '__main__':
   run_streamlit()
