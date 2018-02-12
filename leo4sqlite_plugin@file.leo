<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="tsc.20180211141409.1" a="E"><vh>@settings</vh>
<v t="tsc.20180211195528.1"><vh>@data free-layout-layout</vh></v>
<v t="tsc.20180211141409.2"><vh>@data external tools</vh></v>
<v t="tsc.20180211141409.3"><vh>@string sqlite_output_dir = "/home/tsc/Desktop/leo4sqlite-output"</vh></v>
<v t="tsc.20180211141409.4"><vh>@string sqlite_temp_dir = "/home/tsc/Desktop/leo4sqlite-temp"</vh></v>
<v t="tsc.20180211141409.5"><vh>/home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.6"><vh>/home/tsc/Desktop/leo4sqlite/leo4sqlite.py</vh></v>
<v t="tsc.20180211141409.7"><vh>/home/tsc/Desktop/leo4sqlite-file/leo4sqlite@file.py</vh></v>
</v>
<v t="tscv11.20180119175627.1" a="E"><vh>Sqlite3</vh>
<v t="tsc.20180206152253.2" a="E"
expanded="tsc.20180209235407.1,"><vh>@file /home/tsc/Desktop/leo-editor/leo/plugins/leo4sqlite.py</vh></v>
</v>
<v t="tsc.20180211141409.8"><vh>temp</vh></v>
<v t="tsc.20180211185713.2"><vh>@tbl test</vh></v>
<v t="tsc.20180211141409.9" a="E"><vh>data</vh>
<v t="tsc.20180211203555.1" a="E"><vh>@db3 /home/tsc/Desktop/blob_test.db3</vh>
<v t="tsc.20180211203555.2"><vh>@tbl testorama</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="tsc.20180211141409.1"></t>
<t tx="tsc.20180211141409.2"># one executable per line

xviewer
</t>
<t tx="tsc.20180211141409.3"></t>
<t tx="tsc.20180211141409.4"></t>
<t tx="tsc.20180211141409.5"></t>
<t tx="tsc.20180211141409.6"></t>
<t tx="tsc.20180211141409.7"></t>
<t tx="tsc.20180211141409.8"></t>
<t tx="tsc.20180211141409.9"></t>
<t tx="tsc.20180211185713.2">@language md

'bd', ' cv', ' gdfg'
123, 456.0, 789
abd, dns, lke
789, 456, 123
blue, red, green

column names, column types:

name, amount, date
text, real, text
</t>
<t tx="tsc.20180211195528.1">{
    "content": [
        "_leo_pane:bodyFrame",
        {
            "content": [
                "_leo_pane:outlineFrame",
                "_leo_pane:logFrame"
            ],
            "sizes": [
                309,
                275
            ],
            "orientation": 2
        }
    ],
    "sizes": [
        807,
        547
    ],
    "orientation": 1
}</t>
<t tx="tsc.20180211203555.1"></t>
<t tx="tsc.20180211203555.2">filepath: /home/tsc/Desktop/blob_test.db3

['Words', 'Amount', 'Time', 'Blobs', 'Filename', 'Extension']
['TEXT', 'REAL', 'INTEGER', 'BLOB', 'TEXT', 'TEXT']

'10', 0.08, 1219
'12', 'none', 'never'
'37', 'none', 'never'
'18', 'ounce', 'half past'
'31', 1.0, 2
'32', 1.0, 2
'33', 2.0, 1
'testykulls', 1.0, 2
'baby', 2.0, 3
'71', 3.0, 4
'72', 4.0, 5
'testykullman', 12.0, 0
'bloborific', 15.0, 9
</t>
<t tx="tscv11.20180119175627.1">**leo4sqlite.py plugin**

*This node belongs at the top level of 'leoPlugins.leo'*

|
         
**Notes**

 | 1. This script needs to be streamlined and polished, which I intend to do (in the end I'm a perfectionist). Any suggestions toward that end are welcome!
 
**Issues**
 
 | 3. Data types - column affinity, manifest type, storage type

**Ideas**
    
 | 1. Recent files for blob command dialogs?
 |

**The commands currently added by the plugin are:**

 | sqlite-make-template"
 | sqlite-import-table
 | sqlite-export-table
 | sqlite-open-blob
 | sqlite-view-blob
 | sqlite-insert-blob
 | sqlite-extract-blob
 | sqlite-reset-temp
 | sqlite-clear-data
 | sqlite-purge-files
 |
 
I want to make this the best plugin I can rather than rushing to finish it. Leo deserves no less! Please provide any feedback you can, and don't hesitate to suggest improvements! :-)</t>
</tnodes>
</leo_file>
