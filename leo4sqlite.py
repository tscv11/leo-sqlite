#@+leo-ver=5-thin
#@+node:tsc.20180206152253.2: * @file /home/tsc/Desktop/leo4sqlite-file/leo4sqlite.py
#@@language python
#@+<< version history >>
#@+node:tsc.20180212011016.1: ** << version history >>
'''
# version history
# 
# *leo4sqlite.py*
# 
#  **v.010** - first working version of plugin.
# 
#  **v.011** - the import layout is now saved in the @tbl node so the export layout can be chosen automatically.
# 
#  **v.015** - added 'sqlite-clear-data', 'sqlite-reset-temp', and 'sqlite-purge-files'.
# 
#  **v.016** - fixed a bug in 'sqlite-extract-table', thanks to Terry Brown.
# 
#  **v.020** - added command 'sqlite-edit-blob', which enables the user to edit indvidual text columns for a 'blob'.
# 
#  **v.022** - various small fixes and enhancements suggested by Terry Brown
#  
#  **v.023** - dialogs now have the standard Leo icon in the upper-left hand corner.
#  
#  **v.024** - the 'get external database' dialog now has two improved options: 1) all files   or   2) .db .db3 .sqlite .sqlite3
#  
#  **v.026** - added basic error handling
#  
#  **v.029** - added settings to auto-delete temporary blob files on exiting Leo and updated the documentation.
#  
#  **v.030** - removed the unused Leo4SQLiteController node.
# 
#  **v.031** - subclassed custom exceptions instead of creating a separate class for each error.
#  
#  **v.033** - added sqlite-make-template command, which creates a new outline with all all of the standard nodes needed to use the script.
'''
#@-<< version history >>
#@+<< docstring >>
#@+node:tsc.20180212011036.1: ** << docstring >>
'''
**leo4sqlite v0.50** - by tscv11
|
 
*Introduction:*

| The script 'leo4sqlite.py' is a Leo-specific python script that provides
| basic import/export functionality between Leo outlines and sqlite3 tables
| as well as blob support  (insert, extract, search for a blob by any value in
| any column, view the blob in the render pane or open it with external tools). 

| Imported tables are stored internally as part of the outline, while exported
| tables (and blobs) are stored in sqlite3 database files.

| Imported tables appear as children of the "data" node (the last top-level
| node). To clear this node of accumulated imports, use the command
| 'sqlite-delete-data'.
|

**Layouts**

| Four import layouts can be used to arrange the data in various formats. 


| *For all layouts:*

 |    The @db3 node header contains the path to the database file.  
 
 |    The @tbl node contains: 
 
  |        a) The path to the db file
  |        b) The table's column names and types
  |        c) The layout used         
    
| *layout one:*

 The @tbl node contains all of the above and the table itself.
 
| *layout two:*
 
 | The @tbl node has one child for every row in the table. Each
 | child's headline contains one row.
 
| *layout 3:*
 
 | The @tbl node has a child for each column. Each column node
 | contains all values for that column.
 
| *layout 4:*
 
 | The @tbl node has a child for each column - their headers contain
 | the column names. Their children's headlines each contain one
 | value from the appropriate column.
 |
 
*Blobs*

| Blobs are arranged one per row with the other columns in that row
| containing information about them. The last three columns of each row
| are reserved for the blob, the filename, and the extension, in that order.
| Any number of columns may be added  and used to store additional
| information related to the blob (which will precede it in the table).
|

*Development Status:*

| *This script is functional but still needs plenty of bug-fixing and fine-tuning.*
|

**The commands currently added by the plugin are:**
 |
 | sqlite-make-template
 | sqlite-import-table
 | sqlite-export-table
 | sqlite-import-blobs
 | sqlite-insert-blob
 | sqlite-extract-blob
 | sqlite-view-blob
 | sqlite-open-blob
 | sqlite-edit-blob
 | sqlite-clear-temp
 | sqlite-delete-data
 | sqlite-purge-files
 |

**How to import a table:**

1. Select "import table" as the sqlite3 action to perform.
2. Choose an external database file
3. Pick a table
4. Select a layout

| *Your imported table should now appear. You're welcome.*  :-)
|

**How to export a table:**

1. Select "export table" as the sqlite3 action to perform.
2. Choose an internal database from those found under the "data" node.
3. Select a table.
4. The correct layout will be read from the table automatically.

| *Your exported table should now be written to the sqlite3 db file.*
|

**How to insert a blob**

1. Select "insert blob" as the sqlite3 action to perform.
2. Choose the target external database file.
3. Pick a 'blob table' where the blob will be stored.
4. Enter information for each column in that blob's row.

| *The blob should now be written to the database file.*
|

**How to extract a blob**

1. Select "extract blob" as the sqlite3 action to perform.
2. Choose the external database file containing the blob.
3. Pick the table containing the blob.
4. Enter a search column and search term.

|  *The matching blob should now be extracted to the*
|  *output folder you've specified in the @settings tree.*
|

**How to view a blob**

1. Select "view blob" as the sqlite3 action to perform.
2. Choose the external database containing the blob you wish to view.
3. Pick the table containing the blob.
4. Specify a search column and search term.

| *The matching blob should now be extracted to the temp folder you've*
| *chosen (in the @settings tree). An @image node is then created for the*
| *blob and the render pane is opened to view it.*
|

**How to open a blob**

1. Select "open blob" as the sqlite3 action to perform.
2. Choose the external database containing the blob you wish to view.
3. Pick the table containing the blob.
4. Specify a search column and search term.
5. Choose an external tool to use when opening the file.

| *The matching blob should now be extracted to the temp folder you've*
| *chosen (in the @settings tree). The file is then opened with the selected*
| *external tool.*
|

**sqlite-clear-temp**

| To remove all temporary blob nodes from the temp node use this command.
| This leaves the files intact.


**sqlite-delete-data**

| This command removes all children of the 'data' node, where all imports
| appear. Use caution!


**sqlite-purge-files**

| This command deletes *all* physical files from the 'leo4sqlite-temp' directory.
|


**Settings**

| There are now four @settings nodes which should be created and placed
| in either the current outline's @settings tree or in myLeoSettings.leo.

| The nodes are:

| @string sqlite_output_dir = "<path>" -> Output directory for extracted blobs.
| @string sqlite_tem_dir = "<path>"     -> Temporary folder for viewed blobs.
| @bool del_blobs_on_exit = 1 (yes) **or** 0 (no)

| And finally,

| @data external tools - this node holds paths to external tools for use when
| opening blobs. The format is simply one full path per line, ending in the name
| of an executable.
|

**Outline Template**

*leo4sqlite_template.leo*

| Included with this distribution you'll find a template made for leo4sqlite that
| includes the standard nodes you'll need, ready for customization.
'''
#@-<< docstring >>
#@+<< imports >>
#@+node:tsc.20180209234613.5: ** << imports >>
import leo.core.leoGlobals as g

import glob
import os
import re
import sqlite3
import subprocess

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QDesktopWidget
#@-<< imports >>
#@+others
#@+node:tsc.20180209234613.6: ** onCreate
def onCreate (tag, keys):
    
    c = keys.get('c')
    c._leo4sqlite = {}

    g.registerHandler('end1', delBlobs)
#@+node:tsc.20180209234613.7: ** init
def init ():

    ok = g.app.gui.guiName() in ('qt','qttabs')
    if ok:
        if 1: # Create the commander class *before* the frame is created.
            g.registerHandler('before-create-leo-frame',onCreate)
        else: # Create the commander class *after* the frame is created.
            g.registerHandler('after-create-leo-frame',onCreate)
        g.plugin_signon(__name__)       
    return ok

#@+node:tsc.20180209234613.8: ** class Leo4SqliteError
class Leo4SqliteError(Exception): pass

#@+others
#@+node:tsc.20180209234613.9: *3* class Sqlite3DatabaseError
class Sqlite3DatabaseError(Leo4SqliteError):
    """File is encrypted or is not a database."""
    
#@+node:tsc.20180213194315.1: *3* class TableIsBlobTable
class TableIsBlobTable(Leo4SqliteError):
    """Table is a BLOB table: use 'import-blobs' instead."""
#@+node:tsc.20180209234613.10: *3* class UnknownActionError
class UnknownActionError(Leo4SqliteError):
    """Unknow action error."""
    

#@+node:tsc.20180209234613.11: *3* class NoInternalDBsError
class NoInternalDBsError(Leo4SqliteError):
    """No internal database(s) present."""

#@+node:tsc.20180209234613.12: *3* class NoOutputDirectory
class NoOutputDirectory(Leo4SqliteError):
    """No output directory specified in settings."""

#@+node:tsc.20180209234613.13: *3* class NoTempDirectory
class NoTempDirectory(Leo4SqliteError):
    """No temp directory specified in settings."""

#@+node:tsc.20180209234613.14: *3* class UserCancel
class UserCancel(Leo4SqliteError):
    """Action cancelled by user."""

#@+node:tsc.20180209234613.15: *3* class NodeExists
class NodeExists(Leo4SqliteError):
    """Node already exists. New node not created."""



#@-others
#@+node:tsc.20180209234613.16: ** class InputDialogs
class InputDialogs(QWidget):
    
    #@+others
    #@+node:tsc.20180209234613.17: *3* __init__
    def __init__(self, c):
        super().__init__()
        self.title = 'leo4sqlite'
        self.setWindowIcon(QtGui.QIcon(r'leo/Icons/application-x-leo-outline.png'))
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        try:
            self.initUI(c)
        except Leo4SqliteError as l4serr:
            g.es("\nleo4sqlite plugin: %s\n" % l4serr.__doc__)  
            return
    #@+node:tsc.20180209234613.18: *3* initUI
    def initUI(self, c):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        self.pick_action(c)
     
        self.show() 


    #@+node:tsc.20180209234613.19: *3* pick_action
    def pick_action(self, c):
        
        action = c._leo4sqlite['action']    
            
        cmds = ("get_ext_db select_table get_blob_col")
        
        actions = {
                    "import table": cmds + " get_layout grand_central",
                    "export table": " get_int_dbs select_table get_blob_col grand_central",
                    "import blobs": cmds + " grand_central", 
                    "export blobs": cmds + " grand_central",
                    "insert blob": cmds + " insert_blob",
                    "extract blob": cmds + " extract_blob",
                    "open blob": cmds + " open_blob",
                    "view blob": cmds + " view_blob",
                    "edit blob": cmds + " edit_blob",
             }
        
        if action not in actions:
            raise UnknownActionError()
        for step in actions[action].split():
            method = getattr(self, step)
            method(c)
        

    #@+node:tsc.20180209234613.20: *3* get_ext_db
    def get_ext_db(self, c):
            
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        self.setStyleSheet('padding: 3px; background: white');
        db_fname, _ = QFileDialog.getOpenFileName(self,"select an external database:", "","sqlite files (*.db *.db3 *.sqlite *.sqlite3);;all files (*.*)", options=options) # tnb
        if db_fname == '':
            raise UserCancel()
            return
        else:
            c._leo4sqlite['db_filename'] = db_fname
    #@+node:tsc.20180209234613.21: *3* get_int_dbs
    def get_int_dbs(self, c):
        
        def get_filename(path):
            fn_lst = []
            filename = os.path.basename(path.rstrip('/'))
            fn_lst.append(filename)
            return filename
        
        db3_lst = c.find_h(r'^.*@db3.*$')   

        if db3_lst:
            new_db3_lst = []
            new_db3_cleans = []
            for db3 in db3_lst: 
                new_db3 = re.sub(r'^.*@db3', '', str(db3))
                new_db3 = new_db3[:-1]
                new_db3 = new_db3.lstrip()
                new_db3_lst.append(new_db3)
                new_db3_clean = get_filename(new_db3)
                new_db3_cleans.append(new_db3_clean)

            self.setStyleSheet('padding: 3px; background: white');
            item, okPressed = QInputDialog.getItem(self, "leo4sqlite","choose internal database.", new_db3_lst, 0, False)
            if not okPressed:
                raise NoInternalDBsError
                return
            else:
                c._leo4sqlite['db_filename'] = item


    #@+node:tsc.20180209234613.22: *3* select_table
    def select_table(self, c):

        db_filename = c._leo4sqlite['db_filename']
        tbl_names = []
      
        conn = sqlite3.connect(db_filename)
        res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        
        tbl_nm_str = ''
        for name in res:
            tbl_names.append(name[0])
            tbl_nm_str += "\"" + name[0] + "\", "
        tbl_nm_str = tbl_nm_str[:-3] + "\""

        
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","select a table: ", tbl_names, 0, False)    
        if not okPressed:
                raise UserCancel()
                return
                
        c._leo4sqlite['table_name'] = item
        c._leo4sqlite['tbl_names'] = tbl_names

    #@+node:tsc.20180209234613.23: *3* get_blob_col
    def get_blob_col(self, c):
        
        col_nums = []
        col_names = []
        col_types = []
        num_cols = 0
        file_col = 0
        blob_col = 0
        ext_col = 0
        
        db_filename = c._leo4sqlite['db_filename']
        table_name = c._leo4sqlite['table_name']

        conn = sqlite3.connect(db_filename)
        cur = conn.cursor()
        
        ix = 0
        for row in cur.execute("pragma table_info(" + table_name + ")").fetchall():
        
            col_nums.append(str(row[0]))
            col_names.append(str(row[1]))
            col_types.append(str(row[2]))
        
            if row[2] == "BLOB":
                blob_col = ix
            
            if row[1] == "Filename":
                file_col = ix
            
            if row[1] == "Extension":
                ext_col = ix    
            
            ix = ix + 1
        
        num_cols += len(col_nums) # tnb
        
        c._leo4sqlite['num_cols'] = num_cols
        c._leo4sqlite['col_names'] = col_names
        c._leo4sqlite['col_types'] = col_types
        c._leo4sqlite['col_nums'] = col_nums
        c._leo4sqlite['blob_col'] = blob_col
        c._leo4sqlite['file_col'] = file_col
        c._leo4sqlite['ext_col'] = ext_col
    #@+node:tsc.20180209234613.24: *3* insert_blob
    def insert_blob(self, c):
            
        import os.path
        
        def place_holder(line):
            return '({})'.format(', '.join('?' * len(line)))
        
        col_vals = []
        
        db_filename = c._leo4sqlite['db_filename']
        table_name = c._leo4sqlite['table_name']
        col_names = c._leo4sqlite['col_names']
        
        str_col_names = str(col_names)
        str_col_names = str_col_names[1:-1]

        for i in range(len(col_names)):
            if col_names[i] != "Blobs" and col_names[i] != "Filename" and col_names[i] != "Extension":
                text, okPressed = QInputDialog.getText(self, table_name, col_names[i], QLineEdit.Normal, "")
                if okPressed and text != '':
                    col_vals.append(text)
        
        str_col_names = str(col_names)
        str_col_names = str_col_names[1:-1]
                    
        options = QFileDialog.Options()
        self.setStyleSheet('padding: 3px; background: white');
        blob_filepath, _ = QFileDialog.getOpenFileName(self,"select file to insert:", "","binary files (*)", options=options)
        
        full_filename = os.path.basename(blob_filepath)
        filename, extension = os.path.splitext(full_filename)

        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        
        with open(blob_filepath, "rb") as input_file:
            ablob = input_file.read()
            cells = col_vals
            cells.append(sqlite3.Binary(ablob))
            cells.append(filename)
            cells.append(extension)
            plh = place_holder(cells)
                            
            cursor.execute("insert into " + table_name + " values {} ".format(plh), cells)
            conn.commit()
            
            g.es("\ndone\n")
    #@+node:tsc.20180209234613.25: *3* extract_blob
    def extract_blob(self, c):
        
        ablob = []
        search_items = []

        file_col = c._leo4sqlite['file_col']
        ext_col = c._leo4sqlite['ext_col']
        blob_col = c._leo4sqlite['blob_col']
        col_names = c._leo4sqlite['col_names']
        table_name = c._leo4sqlite['table_name']
        db_filename = c._leo4sqlite['db_filename']

        sqlite_out_dir = c.config.getString("sqlite_output_dir")
        
        if not sqlite_out_dir:
            raise NoOutputDirectory
            return
        
        sqlite_out_dir = sqlite_out_dir[1:-1]
        
        items = (col_names)
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","select column to search:", items, 0, False)
        
        search_col = item
        
        items = []    
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","choose a search term:", items, 0, False)
        
        search_term = item
        
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        
        i = 0
        for row in cursor.execute("SELECT * FROM " + table_name):
            if col_names[i] == search_col:
                search_items.append(row[i])
        
        cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term]) # tnb
        row = cursor.fetchone()
        filename = os.path.basename(row[file_col])
        extension = row[ext_col]
        
        
        filepath = sqlite_out_dir + '/' + filename + extension
        
        with open(filepath, "wb") as output_file:   
            cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term]) # tnb
            ablob = cursor.fetchone()
            output_file.write(ablob[blob_col])
            cursor.close()
        
        conn.close()
        g.es("\ndone\n")
    #@+node:tsc.20180209234613.26: *3* open_blob
    def open_blob(self, c):
        
        items = []
        
        ext_col = c._leo4sqlite['ext_col']
        blob_col = c._leo4sqlite['blob_col']
        file_col = c._leo4sqlite['file_col']
        col_names = c._leo4sqlite['col_names']
        table_name = c._leo4sqlite['table_name']
        db_filename = c._leo4sqlite['db_filename']
        
        sqlite_temp_dir = c.config.getString('sqlite_temp_dir')
        
        if not sqlite_temp_dir:
            raise NoTempDirectory
            return
        
        
        
        p = g.findNodeAnywhere(c, '@data external tools')
        c.selectPosition(p)
        tools = re.split(r'\n', p.b)
        tools = tools[2:-1]
        c.selectThreadBack()
        c.redraw()
        
        items = (col_names)
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","select column to search:", items, 0, False)
        search_col = item
        
        items = []
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","choose a search term:", items, 0, False)
        search_term = item
                              
        self.setStyleSheet('padding: 3px; background: white');
        item, okPressed = QInputDialog.getItem(self, "leo4sqlite","select external tool:", tools, 0, False)
        ext_tool = item
        
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        
        cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term])
        row = cursor.fetchone()
        filename = row[file_col]
        filename = os.path.basename(filename)
        extension = row[ext_col]

        filepath = (sqlite_temp_dir + '//' + filename + extension)

        with open(filepath, "wb") as output_file:        
            cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term])
            ablob = cursor.fetchone()
            output_file.write(ablob[blob_col])
            cursor.close()

            p = subprocess.Popen([ext_tool, filepath])
    #@+node:tsc.20180209234613.27: *3* view_blob
    def view_blob(self, c):

        img_types = ['.png', '.jpg', '.bmp', '.gif']
        vid_types = ['.mp4', '.avi', '.wmv', '.flv', '.mov', '.mkv']
        
        file_col = c._leo4sqlite['file_col']
        ext_col = c._leo4sqlite['ext_col']
        blob_col = c._leo4sqlite['blob_col']
        col_names = c._leo4sqlite['col_names']
        
        table_name = c._leo4sqlite['table_name']
        db_filename = c._leo4sqlite['db_filename']
        
        temp_dir = c.config.getString("sqlite_temp_dir")
        if not temp_dir:
            raise NoTempDirectory
            return
            
        temp_dir = temp_dir[1:-1]
        
        def get_extension(path):
            extension = os.path.splitext(path)[1]
            return extension
        
        def get_filename(path):
            filename = os.path.basename(path)
            return filename    
            
        items = col_names
        self.setStyleSheet('padding: 3px; background: white');
        col, okPressed = QInputDialog.getItem(self, "leo4sqlite","select column to search:", items, 0, False)
        search_col = col
        
        items = []
        self.setStyleSheet('padding: 3px; background: white');
        term, okPressed = QInputDialog.getItem(self, "leo4sqlite","choose a search term:", items, 0, False)
        search_term = term
        
        ablob = []
        
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        
        cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term]) 
        row = cursor.fetchone()
        filename = row[file_col]
        extension = row[ext_col]

        filepath = temp_dir + "/" + filename + extension

        with open(filepath, "wb") as output_file:               
            cursor.execute("select * from %s where %s = ?" % (table_name, search_col), [search_term]) 
            ablob = cursor.fetchone()
            output_file.write(ablob[blob_col])
            cursor.close()
            
            if extension in img_types: 
                ph2b =  (r"@image " + filename + extension)
            if extension in vid_types:
                ph2b =  (r"@movie " + filename + extension)
                
            p = g.findNodeAnywhere(c, "temp")
            c.selectPosition(p)
            
            for child in p.children():
                if child.h == ph2b:
                    c.selectPosition(child)
                    c.executeMinibufferCommand('vr-show')
                    raise NodeExists()
                    return
            
            p = p.insertAsLastChild()
            c.selectPosition(p)
            p.h = ph2b
            p.b = filepath
            
            c.executeMinibufferCommand('vr-show')
            c.redraw()
            p = p.parent() 
            c.redraw()    
    #@+node:tsc.20180209234613.28: *3* edit_blob
    def edit_blob(self, c):
        
        def place_holder(line):
            return '({})'.format(', '.join('?' * len(line)))
            
        col_names = c._leo4sqlite['col_names']
        table_name = c._leo4sqlite['table_name']
        db_filename = c._leo4sqlite['db_filename']
        
        names = []

        self.setStyleSheet('padding: 3px; background: white');
        name, okPressed = QInputDialog.getItem(self, "leo4sqlite","enter blob name:", names, 0, False)
        blob_name = name
        
        cols = (col_names)

        self.setStyleSheet('padding: 3px; background: white');
        col, okPressed = QInputDialog.getItem(self, "leo4sqlite","select column name:", cols, 0, False)
        edit_col = col
        
        values = []
        
        self.setStyleSheet('padding: 3px; background: white');
        value, okPressed = QInputDialog.getItem(self, "leo4sqlite", "enter new value:", values, 0, False)
        new_val = value
        
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        
        cursor.execute("update %s set %s = %s where Filename = ?" % (table_name, edit_col, new_val), [blob_name])
        conn.commit()

        g.es('done')
    #@+node:tsc.20180209234613.29: *3* get_layout
    def get_layout(self, c):
        
        action = c._leo4sqlite['action']
        table_name = c._leo4sqlite['table_name']    
        
        if action == 'import table':
            items = ('one', 'two', 'three', 'four')
            self.setStyleSheet('padding: 3px; background: white');
            item, okPressed = QInputDialog.getItem(self, "leo4sqlite","choose a layout: ", items, 0, False)
            if not okPressed:
                raise UserCancel
                return

            c._leo4sqlite['layout'] = item

        if action == 'export table':
            tbl_h = "@tbl " + str(table_name)
            p = g.findNodeAnywhere(c, tbl_h)
            c.selectPosition(p)
            lines = re.split(r'\n', p.b)
            line = lines[5]
            layout = line[8:]
            c._leo4sqlite['layout'] = layout
            g.es('layout: ' + str(layout))
    #@+node:tsc.20180209234613.30: *3* grand_central
    def grand_central(self, c):
        
        db_filename = c._leo4sqlite['db_filename']
        col_names = c._leo4sqlite['col_names']
        col_nums = c._leo4sqlite['col_nums']
        col_types = c._leo4sqlite['col_types']
        blob_col = c._leo4sqlite['blob_col']
        layout = c._leo4sqlite['layout']
        action = c._leo4sqlite['action']
            
        if action == "export blobs":
            export_blobs(self, c, col_nums, col_names, col_types, blob_col)
        
        #if blob_col:
            #raise TableIsBlobTable
            #return
        
        db3_h = "@db3 " + str(db_filename)
        p = g.findNodeAnywhere(c, db3_h)
        
        if p:
            c.selectPosition(p)
        else:    
            p = c.lastTopLevel().insertAsNthChild(1)
            p.h = "@db3 " + str(db_filename)
            c.redraw(p)
        
        p = p.insertAsNthChild(1)
        p.h = "@tbl " + str(c._leo4sqlite['table_name'])
        c.selectPosition(p)
        c.redraw(p)
        
        if action == "import blobs":   
            p = p.lastNode()
            c.selectPosition(p)
            import_blobs(self, c, p, col_nums, col_names, col_types, blob_col)
        
        if action == "import table" and blob_col:
            raise TableIsBlobTable
            return
            
        if action == "import table":
            if layout == "one":
                import_table1(c, p, col_nums, col_names, col_types, blob_col)
        
            if layout == "two":
                import_table2(c, p, col_nums, col_names, col_types, blob_col)
                
            if layout == "three":
                import_table3(c, p, col_nums, col_names, col_types, blob_col)
            
            if layout == "four":
                import_table4(c, p, col_nums, col_names, col_types, blob_col)
                   
        
        if action == 'export table' and blob_col:
            raise TableIsBlobTable
            return
            
            p = c.p
                
            if layout == "one":
                export_table1(self, c, p, col_nums, col_names, col_types, blob_col)
            
            if layout == "two":
                export_table2(self, c, p, col_nums, col_names, col_types, blob_col)
                
            if layout == "three":
                export_table3(self, c, p, col_nums, col_names, col_types, blob_col)
                
            if layout == "four": 
                export_table4(self, c, p, col_nums, col_names, col_types, blob_col)
    #@-others
#@+node:tsc.20180209235407.1: ** import_tables
#@+others
#@+node:tsc.20180209234613.31: *3* import_table1
def import_table1(c, p, col_nums, col_names, col_types, blob_col):

    table_name = c._leo4sqlite['table_name']
    filepath = c._leo4sqlite['db_filename']
    layout = c._leo4sqlite['layout']
    
    num_cols = 0
    for col in col_nums:
        num_cols = num_cols + 1
    
    g.es("\nimporting table: " + table_name + "\n\n(layout 1)\n")
                    
    rx = 0
    delim = ", "
    new_row = ""
    
    p.b = p.b + "filepath: " + str(filepath) + "\n\n"
    p.b = p.b + str(col_names) + "\n"
    p.b = p.b + str(col_types) + "\n\n"
    p.b = p.b + str("layout: " + layout) + "\n\n"

    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM " + table_name):
    
        cx = 0 
        if row != "":
            cols = re.split(delim, str(row))

            ix = 0
            for col in cols:
                if col != "":
                    new_row = new_row + col + ", "
                    cx = cx + 1
                new_row = re.sub(r'[\"]', " ", str(new_row))   
                                
            p.b = p.b + str(new_row[1:-3]) + "\n"
            new_row = ""
            rx = rx + 1       
    
    g.es("done\n")
    c.redraw()
    headline = ("@tbl " + table_name)    
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
#@+node:tsc.20180209234613.32: *3* import_table2
def import_table2(c, p, col_nums, col_names, col_types, blob_col):

    db_filename = c._leo4sqlite['db_filename']
    table_name = c._leo4sqlite['table_name']
    layout = c._leo4sqlite['layout']

    num_cols = 0
    for col in col_nums:
        num_cols = num_cols + 1
    
    idx = 0
    rx = 0
    
    p.b = p.b + "filepath: " + str(db_filename) + "\n\n"
    p.b = p.b + str(col_names) + "\n"
    p.b = p.b + str(col_types) + "\n\n"
    p.b = p.b + 'layout: ' + layout + '\n\n'
    
    g.es("\nimporting table: " + table_name + "\n\n(layout 2)\n")

    rows = []
    
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM " + table_name):    
        rows.append(row)
    
        idx = idx + 1  
        if idx == 1:
            p = p.insertAsNthChild(1)
            c.selectPosition(p)
        else:
            p = p.insertAfter()
            c.selectPosition(p)

        delim = ","
        new_row = ""
        
        rx = rx + 1
        if row != "":
            cols = re.split(delim, str(row))
            for col in cols:
                new_row = new_row + col + ","
            new_row = re.sub(r'[\"\'\s]', "", str(new_row))
            final_row = re.sub(r',', ", ", str(new_row))
        p.h = str(final_row[1:-3])
    
    g.es("\ndone\n")
    c.redraw()        
    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
#@+node:tsc.20180209234613.33: *3* import_table3
def import_table3(c, p, col_nums, col_names, col_types, blob_col):

    db_filename = c._leo4sqlite['db_filename']
    table_name = c._leo4sqlite['table_name']
    layout = c._leo4sqlite['layout']
    
    g.es("\nimporting table: " + table_name + "\n\n(layout 3)\n")

    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("select * from " + table_name)
    row = cursor.fetchone()
    names = row.keys()

    rx = 0
    cx = 0
    num_cols = 0

    p.b = p.b + "filepath: " + str(db_filename) + "\n\n"
    p.b = p.b + str(col_names) + "\n"
    p.b = p.b + str(col_types) + "\n\n"    
    p.b = p.b + 'layout: ' + layout + '\n\n'

    for col_num in col_nums:
        num_cols = num_cols + 1
    
    cx = 0
    for col_name in names:
        if cx == 0:
            p = p.insertAsLastChild()
        else:
            p = p.insertAfter()
        
        p.h = col_name
        c.redraw()
        
        rx = 0
        rows = []
        for row in cursor.execute("SELECT * FROM " + table_name):
            rows.append(str(row[cx]))
            p.b = p.b + (str(row[cx]) + "\n")
            rx = rx + 1            
            
        cx = cx + 1

    g.es("done\n")
        
    c.redraw()
    headline = ("@tbl " + table_name)    
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
#@+node:tsc.20180209234613.34: *3* import_table4
def import_table4(c, p, col_nums, col_names, col_types, blob_col):

    db_filename = c._leo4sqlite['db_filename']
    table_name = c._leo4sqlite['table_name']
    layout = c._leo4sqlite['layout']
    
    g.es("\nimporting table: " + table_name + "\n\n(layout 4)\n")

    num_cols = 0
    for col_num in col_nums:
        num_cols = num_cols + 1

    idx = 0

    p.b = p.b + "filepath: " + str(db_filename) + "\n\n"
    p.b = p.b + str(col_names) + "\n"
    p.b = p.b + str(col_types) + "\n\n"
    p.b = p.b + 'layout: ' + layout + '\n\n'
    
    for col_name in col_names:
        if idx == 0:
            p = p.insertAsLastChild()
        else:
            p = p.insertAfter()
            
        p.h = col_name
    
        i = 0
        rx = 0
        cx = 0
        rows = []
        
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("select * from " + table_name)
        results = cursor.fetchall()
        num_rows = len(results)
        
        while rx < num_rows:
            for row in cursor.execute("select * from " + table_name):
                if i == 0:
                    p = p.insertAsLastChild()
                else:
                    p = p.insertAfter()
                            
                new_row = re.sub(r'[\(\)\"]', " ", str(row))
                new_row = new_row.lstrip()
                new_row = re.split(r',', new_row)
                rows.append(new_row)
                
                p.h = str(rows[rx][cx + idx])
                
                i = i + 1
                rx += 1

            p = p.parent()   
            if idx >= num_rows:
                break
            new_row = re.sub(r'[\[\]\'\"\s]', "", str(rows[idx]))        
            new_row = re.sub(r',', ", ", new_row) 
            cx += 1
        idx += 1
    
    p = p.parent()
    p.contract()

    g.es("done\n")
    c.redraw()
    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)

#@-others
#@+node:tsc.20180209235541.1: ** export_tables
#@+others
#@+node:tsc.20180209234613.35: *3* export_table1
def export_table1(self, c, p, col_nums, col_names, col_types, blob_col):
    
    def place_holder(line):
        return '({})'.format(', '.join('?' * len(line)))
    
    table_name = c._leo4sqlite['table_name']

    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))        
    c.selectPosition(tbl_node)
    c.redraw()
    p = c.p
    
    g.es("\nexporting table " + table_name + "\n\n(layout 1)\n")

    lines = re.split("\n", p.b)

    new_names = re.sub(r'[\"\'\[\]\s]', "", str(col_names))
    new_types = re.sub(r'[\"\'\[\]\s]', "", str(col_types))

    split_names = re.split(r',', str(new_names))
    split_types = re.split(r',', str(new_types))
    
    sql = "("
    for i in range(len(split_names)):
        sql = sql + split_names[i] + " " + split_types[i] + ", "
    sql = sql[:-2]
    sql = sql + (")")

    lines = lines[7:]
    
    db_filename = c._leo4sqlite['db_filename']
    
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    statement = "SELECT name FROM sqlite_master WHERE type='table';"
    if (table_name,) in cur.execute(statement).fetchall():
        overwrite = g.app.gui.runAskYesNoDialog(c, "overwrite existing table?", message="a table by that name already exists.\nreplace it with current table?") 
        if overwrite == "no":
            print("cancelled\n")
            return
        print("table: '%s' exists" % table_name)
        cur.execute("DROP TABLE " + table_name)
        print("\ndropping old table")
    cur.execute("CREATE TABLE " + table_name + " " + sql)
    print("creating new table")

    for line in lines:    
        if line != "":
            cells = re.split(",", line)         
            plh = place_holder(cells)
            cur.execute("insert into " + table_name + " values {} ".format(plh), cells)
            conn.commit()
        else:
            g.es("\ndone\n")
            return
#@+node:tsc.20180209234613.36: *3* export_table2
def export_table2(self, c, p, col_nums, col_names, col_types, blob_col):
    
    hlines = []
    table_name = c._leo4sqlite['table_name']
    db_filename = c._leo4sqlite['db_filename']
   
    def place_holder(line):
        return '({})'.format(', '.join('?' * len(line)))

    g.es("\nexporting table: " + table_name + "\n\n(layout 2)\n") 

    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
    c.redraw()
    p = c.p
    lines = re.split(r"\n", p.b)
    names = lines[2]
    types = lines[3]
    
    for p in p.children():
        hlines.append(p.h)
    
    new_names = re.sub(r'[\"\'\[\]\s]', "", str(names))
    new_types = re.sub(r'[\"\'\[\]\s]', "", str(types))
    
    split_names = re.split(r',', str(new_names))
    split_types = re.split(r',', str(new_types))

    sql = "("
    for i in range(len(split_names)):
        sql = sql + split_names[i] + " " + split_types[i] + ", "
    sql = sql[:-2]
    sql = sql + (")")

    lines = lines[7:]
    
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    statement = "SELECT name FROM sqlite_master WHERE type='table';"
    if (table_name,) in cur.execute(statement).fetchall():
        overwrite = g.app.gui.runAskYesNoDialog(c, "overwrite existing table?", message="a table by that name already exists.\nreplace it with current table?") 
        if overwrite == "no":
            print("cancelled\n")
            return
        print("table: '%s' exists" % table_name)
        cur.execute("DROP TABLE " + table_name)
        print("\ndropping old table")
    cur.execute("CREATE TABLE " + table_name + " " + sql)
    print("creating new table")
    
    for line in hlines:    
        if line != "":
            cells = re.split(",", line)
            
            plh = place_holder(cells)
            cur.execute("insert into " + table_name + " values {} ".format(plh), cells)
            conn.commit()
    g.es("\ndone\n")
#@+node:tsc.20180209234613.37: *3* export_table3
def export_table3(self, c, p, col_nums, col_names, col_types, blob_col):

    def place_holder(line):
        return '({})'.format(', '.join('?' * len(line)))

    table_name = c._leo4sqlite['table_name']
    db_filename = c._leo4sqlite['db_filename']
    layout = c._leo4sqlite['layout']
    
    g.es("\nexporting table: " + table_name + "\n\n(layout 3)\n") 
    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
    c.redraw()
    p = c.p
    lines = re.split(r'\n', str(p.b))
    names = lines[2]
    types = lines[3]

    new_names = re.sub(r'[\"\'\[\]\s]', "", str(names))
    new_types = re.sub(r'[\"\'\[\]\s]', "", str(types))
    split_names = re.split(r',', str(new_names))
    split_types = re.split(r',', str(new_types))

    row = []
    rows = []
    cols = []
    num_rows = 0
    num_cols = 0
    split_blines = []
    clean_blines = []
      
    for p in p.children():

        split_blines = re.split(r'\n', p.b)
        num_rows = (len(split_blines))
        clean_blines = re.sub(r'[\'\[\]\s]', "", str(split_blines))
        clean_blines = clean_blines[:-1]
        clean_blines = re.split(r',', clean_blines)
        cols.append(clean_blines)
        num_cols = num_cols + 1
    
    sql = "("
    for i in range(len(split_names)):
        sql = sql + split_names[i] + " " + split_types[i] + ", "
    sql = sql[:-2]
    sql = sql + (")")

    lines = lines[7:]

    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    statement = "SELECT name FROM sqlite_master WHERE type='table';"
    if (table_name,) in cur.execute(statement).fetchall():
        overwrite = g.app.gui.runAskYesNoDialog(c, "overwrite existing table?", message="a table with that name already exists.\nreplace it with current table?") 
        if overwrite == "no":
            print("cancelled\n")
            return
        print("table: '%s' exists" % table_name)
        cur.execute("DROP TABLE " + table_name)
        print("\ndropping old table")
    cur.execute("CREATE TABLE " + table_name + " " + sql)
    print("creating new table")
    
    x = 0
    z = 0
    row = []
    rows = []
    while x < num_rows - 1:
        for i in range(len(cols)):
            row.append((cols[i][x]))
        row = re.sub(r'[\[\]\'\"\s]', "", str(row))
        row = re.sub(r',', ", ", row) 
        row = re.split(r',', row)
        cells = row[:int(num_cols)]
        plh = place_holder(cells)
        cur.execute("insert into " + table_name + " values {} ".format(plh), cells)
        conn.commit()
        rows = rows[num_cols:]
        z += 1

        rows.append(row)
        row = row[num_cols:]
        x += 1    
    
    row = rows[0][:num_cols]
    row = rows[0][num_cols:num_cols * num_rows]
    
    row = row[num_cols:]
            
    g.es("\ndone\n")
#@+node:tsc.20180209234613.38: *3* export_table4
def export_table4(self, c, p, col_nums, col_names, col_types, blob_col):
    
    def place_holder(line):
        return '({})'.format(', '.join('?' * len(line)))

    col_hlines = []
    row_hlines = []
    
    db_filename = c._leo4sqlite['db_filename']
    table_name = c._leo4sqlite['table_name']
    
    g.es("\nexporting table: " + table_name + "\n\n(layout 4)\n") 
    headline = ("@tbl " + table_name)
    tbl_node = g.findNodeAnywhere(c, (headline))
    c.selectPosition(tbl_node)
    c.redraw()
    p = c.p
    
    lines = re.split(r'\n', str(p.b))
  
    for p in p.children():
        col_hlines.append(p.h)
        for p in p.children():
            row_hlines.append(p.h)

    num_cols = len(col_hlines)
    num_rows =int(len(row_hlines) / num_cols)

    new_names = re.sub(r'[\"\'\[\]\s]', "", str(col_names))
    new_types = re.sub(r'[\"\'\[\]\s]', "", str(col_types))
    
    split_names = re.split(r',', str(new_names))
    split_types = re.split(r',', str(new_types))
    
    sql = "("
    for i in range(len(split_names)):
        sql = sql + split_names[i] + " " + split_types[i] + ", "
    sql = sql[:-2]
    sql = sql + (")")
    
    lines = lines[7:]
    
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    
    statement = "SELECT name FROM sqlite_master WHERE type='table';"
    if (table_name,) in cur.execute(statement).fetchall():
        overwrite = g.app.gui.runAskYesNoDialog(c, "overwrite existing table?", message="a table by that name already exists.\nreplace it with current table?") 
        if overwrite == "no":
            print("cancelled\n")
            return
        print("table: '%s' exists" % table_name)
        cur.execute("DROP TABLE " + table_name)
        print("\ndropping old table")
    cur.execute("CREATE TABLE " + table_name + " " + sql)
    print("creating new table\n")
    
    i = 0
    x = 0
    row = []
    lines = []
    while x < num_rows:
        for i in range(len(col_hlines)):
            row.append(row_hlines[i * num_rows + x])
            i += num_cols
        if row:
            plh = place_holder(row)
            cur.execute("insert into " + table_name + " values {} ".format(plh), row)
            conn.commit()
        row = row[num_cols:]
        x+= 1
    
    g.es("done\n")
#@-others
#@+node:tsc.20180214062647.1: ** import_blobs
def import_blobs(self, c, p, col_nums, col_names, col_types, blob_col):

    table_name = c._leo4sqlite['table_name']
    filepath = c._leo4sqlite['db_filename']

    num_cols = len(col_nums)
    primary_key_col = num_cols - 4
    filename_col = num_cols - 2
    extension_col = num_cols - 1

    g.es("\nimporting blob table: " + table_name + "\n")

    p.b += str(col_names) + "\n"
    p.b += str(col_types) + "\n\n"
    node_name = p.h

    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM " + table_name):

        new_row = ""
        for cx, col in enumerate(row):
            if cx == primary_key_col:
                break
            if col != "" and col_types[cx] != "BLOB":
                new_row += "%s: %s\n" % (col_names[cx], col)

        nd = p.insertAsLastChild()
        nd.h = row[filename_col] + row[extension_col]
        nd.b = new_row

    g.es("done\n")
    c.redraw()
    c.selectPosition(g.findNodeAnywhere(c, node_name))
#@+node:tsc.20180209234613.39: *3* @@import_blobs
#@+at
# def import_blobs(self, c, p, col_nums, col_names, col_types, blob_col):
#     
#     table_name = c._leo4sqlite['table_name']
#     filepath = c._leo4sqlite['db_filename']
#     
#     num_cols = 0
#     for col in col_nums:
#         num_cols = num_cols + 1
#  
#     filename_col = num_cols - 2
#     extension_col = num_cols -1
#     
#     g.es("\nimporting blob table: " + table_name + "\n")
#          
#     delim = ", "
#     new_row = ""
#     
#     #p.b = p.b + "filepath: " + str(filepath) + "\n\n"
#     p.b = p.b + str(col_names) + "\n"
#     p.b = p.b + str(col_types) + "\n\n"
#     
#     conn = sqlite3.connect(filepath)
#     cursor = conn.cursor()
#     for row in cursor.execute("SELECT * FROM " + table_name):
#     
#         rx = 0 
#         if row != "":
#             cols = re.split(delim, str(row))
# 
#             cx = 0
#             for col in cols:
#                 if col != "" and col_types[cx] != "BLOB":
#                     if cx == 0: col = col[1:]
#                     new_row = new_row + col_names[cx] + ": " + col + "\n"
#                     cx = cx + 1
#                 new_row = re.sub(r'[\"]', " ", str(new_row))   
#              
#             if rx < 3:                    
#                 p = p.insertAsLastChild()
#                 cx = 0
#             else:
#                 p = p.insertAfter()
#             
#             rx + 1
#                 
#             c.selectPosition(p)
#             p.h = row[filename_col] + row[extension_col]
#             #p.b = p.b + str(filepath) + "\n\n"
#             p.b = p.b + str(new_row[:-1]) + "\n"
#             new_row = ""
# 
#     g.es("done\n")
#     c.redraw()
#     headline = ("@tbl " + table_name)    
#     tbl_node = g.findNodeAnywhere(c, (headline))
#     c.selectPosition(tbl_node)
#@+node:tsc.20180216194402.1: ** export_blobs
def export_blobs(self, c, col_nums, col_names, col_types, blob_col):
    
    '''export table with any text field changes included.'''
    
    def place_holder(line):
        return '({})'.format(', '.join('?' * len(line)))
    
    import re
    import sqlite3
    
    keys = []
    vals = []
    key_lst = []
    val_lst = []
    child_h = []
    child_b = []
    new_row = ''
    
    p = c.p
    parent = p.parent()
    c.selectPosition(parent)
    table_name = re.sub(r'^@tbl\s', '', parent.h)
    g.es(table_name)
    
    p = p.parent()
    c.selectPosition(p)
    
    p = p.parent()
    c.selectPosition(p)
    filename = p.h[5:]
    g.es(filename)
    
    p = p.firstChild()
    c.selectPosition(p)
    
    for child in p.children():
        child_h.append(child.h)
        child_b = re.split(r'\n', str(child.b))
    
    children = parent.children()
    for child in children:
        child_b = re.split(r'\n', child.b)
        for line in child_b:
            line = re.sub(r'^.*match=', '', line)
            key_val = re.split(r':\s', line)
            
            i = 0
            for field in key_val:
                if i == 0 and field != "":
                    key_lst.append(field)
                else:
                    if i == 1 and field != "":
                        val_lst.append(field)
                i += 1
    
    num_cols = len(child_b) - 1
    
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    
    rx = 1    
    cur.execute("select * from %s" % (table_name))
    rows = cur.fetchall()
    for row in rows:    
    
        keys = key_lst[:num_cols]
        vals = val_lst[:num_cols]
        
        cx = 0
        for key in keys:
                
            query = "update %s set %s = ? where Primary_Key = ?" % (table_name, keys[cx])
            cur.execute(query, [vals[cx], rx])
            cx += 1
        
        key_lst = key_lst[num_cols:]
        val_lst = val_lst[num_cols:]
        rx += 1
            
    conn.commit()
    conn.close()
#@+node:tsc.20180217214035.1: *3* @@export_blobs_bak
#@+at
# import sqlite3
# 
# col_names = ["one", "two", "three", "one", "two", "three"]
# key_lst = ["one", "two", "three", "one", "two", "three"]
# val_lst = ["red", "blue", "green", "white", "black", "blue"]
# 
# num_cols = 3
# 
# filename = "/home/tsc/Desktop/blob_test.db3" # your filename here
# table_name = "testorama" # your table name here
# 
# conn = sqlite3.connect(filename)
# cur = conn.cursor()
# 
# rx = 1    
# cur.execute("select * from %s" % (table_name))
# rows = cur.fetchall()
# for row in rows:    
#     
#     keys = key_lst[:num_cols]
#     vals = val_lst[:num_cols]
#     
#     #g.es(vals)
#     
#     cx = 0
#     for key in keys:
#             
#         query = "update %s set %s = ? where Primary_Key = ?" % (table_name, keys[cx])
#         cur.execute(query, [vals[cx], rx])
#         cx += 1
#     
#     key_lst = key_lst[num_cols:]
#     val_lst = val_lst[num_cols:]
#     rx += 1
#     
#     g.es(key_lst)
#     g.es(val_lst)
#         
# conn.commit()
# conn.close()
#@+node:tsc.20180221104553.1: *3* @@export_blobs_bak
#@+at
# import sqlite3
# 
# col_names = ["one", "two", "three", "four", "five", "six"]
# key_lst = ["one", "two", "three", "four", "five", "six"]
# val_lst = ["green", "white", "black", "yellow", "red", "blue"]
# 
# num_cols = 3
# 
# filename = "/home/tsc/Desktop/blob_test.db3" # your filename here
# table_name = "testorama" # your table name here
# 
# conn = sqlite3.connect(filename)
# cur = conn.cursor()
# 
# rx = 1    
# for row in cur.execute("SELECT * FROM %s " % table_name):
#     
#     keys = key_lst[:num_cols]
#     vals = val_lst[:num_cols]
#     
#     g.es(vals)
#     
#     cx = 0
#     for key in keys:
#             
#         query = "update %s set %s = ? where Primary_Key = ?" % (table_name, keys[cx])
#         cur.execute(query, [vals[cx], rx])
#         cx += 1
#         
#     key_lst = key_lst[num_cols:]
#     val_lst = val_lst[num_cols:]
#     rx += 1
#     
# conn.commit()
# conn.close()
#@+node:tsc.20180221111226.1: *3* @@export_blobs_bak
#@+at
# import sqlite3
# 
# col_names = ["one", "two", "three", "one", "two", "three"]
# key_lst = ["one", "two", "three", "one", "two", "three"]
# val_lst = ["green", "white", "black", "yellow", "red", "blue"]
# 
# num_cols = 3
# 
# filename = "/home/tsc/Desktop/blob_test.db3" # your filename here
# table_name = "testorama" # your table name here
# 
# conn = sqlite3.connect(filename)
# cur = conn.cursor()
# 
# rx = 1    
# #for row in cur.execute("SELECT * FROM %s" % table_name):
# cur.execute("select * from %s" % (table_name))
# rows = cur.fetchall()
# for row in rows:    
#     
#     keys = key_lst[:num_cols]
#     vals = val_lst[:num_cols]
#     
#     #g.es(vals)
#     
#     cx = 0
#     for key in keys:
#             
#         query = "update %s set %s = ? where Primary_Key = ?" % (table_name, keys[cx])
#         cur.execute(query, [vals[cx], rx])
#         cx += 1
#     
#     key_lst = key_lst[num_cols:]
#     val_lst = val_lst[num_cols:]
#     rx += 1
#     
#     g.es(key_lst)
#     g.es(val_lst)
#         
# conn.commit()
# conn.close()
#@+node:tsc.20180209234613.41: ** delete_blobs
def delBlobs(c): 
    
    del_blobs_on_exit = c.config.getBool('del_blobs_on_exit')
    
    if del_blobs_on_exit == 1:
        sqlite_temp_dir = c.config.getString('sqlite_temp_dir') 
            
        os.chdir(sqlite_temp_dir)
        files=glob.glob('*')
        if files:
            for filename in files:
                os.unlink(filename)
#@+node:tsc.20180209235759.1: ** @g.commands
#@+others
#@+node:tsc.20180209234613.42: *3* sqlite_make_template
@g.command('sqlite-make-template')
def sqlite_make_template(event):
    
    template = [
        ("@settings", "Please customize...", [
            ("@string sqlite_temp_dir = ~/leo4sqlite-temp", "Enter the full path...", []),
            ("@string sqlite_output_dir = ~/leo4sqlite-output", "Enter the full path.", []),
            ("@bool del_blobs_on_exit = False", "Delete blobs extracted for viewing.", []),
            ("@data external tools", "# leave one blank line at the end of this body text\n\nExamples for linux:\n\n/usr/bin/gimp\n/usr/bin/xviewer\n", []),
            ("@commands", "Examples of hotkeys. Command names are in the docstring.", [
                ("@command sqlite-clear-temp @key Alt-Shift-Ctrl-t", "c.executeMinibufferCommand('sqlite-clear-temp'", [
                    ("@test child", "something", []),
                    ("@test child2", "something else", []),
                ]),
                ("@command sqlite-delete-data @key Alt-Shift-Ctrl-d", "c.executeMinibufferCommand('sqlite-delete-data')", []),
                ("@command sqlite-purge-files @key Alt-Shift-Ctrl-p", "c.executeMinibufferCommand('sqlite-purge-files')", []),
            ]),
        ]),
        ("temp", "Clean up temporary nodes.", []),
        ("data", "This node must be the last top level node.", []),
    ]
    
    c = event.get('c')
    c = c.new({}, gui=g.app.gui)
    
    p = c.p
    p.h = "leo4sqlite template"
    
    def mknode(nd, data):
        head, body, children = data
        nd.h = head
        nd.b = body
        for child in children:
            mknode(nd.insertAsLastChild(), child)
    
    for data in reversed(template):
        mknode(p.insertAfter(), data)
   
    c.redraw()
#@+node:tsc.20180209234613.43: *3* sqlite_import_table
@g.command('sqlite-import-table')
def sqlite_import_table(event):
    
    c = event.get('c')
    
    action = "import table"
    c._leo4sqlite['action'] = action

    InputDialogs(c)
#@+node:tsc.20180209234613.44: *3* sqlite_export_table
@g.command('sqlite-export-table')
def sqlite_export_table(event):
    
    c = event.get('c')
    
    action = "export table"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
#@+node:tsc.20180209234613.45: *3* sqlite_import_blobs
@g.command('sqlite-import-blobs')
def sqlite_import_blobs(event):
    
    c = event.get('c')
    
    c._leo4sqlite['action'] = "import blobs"
    c._leo4sqlite['layout'] = "one"    
    
    InputDialogs(c)

#@+node:tsc.20180209234613.46: *3* sqlite_export_blobs
@g.command('sqlite-export-blobs')
def sqlite_export_blobs(event):
    
    c = event.get('c')
    
    c._leo4sqlite['action'] = "export blobs"
    c._leo4sqlite['layout'] = "one"    
    
    InputDialogs(c)

#@+node:tsc.20180209234613.47: *3* sqlite_insert_blob
@g.command('sqlite-insert-blob')
def sqlite_insert_blob(event):   
    
    c = event.get('c')
    
    action = "insert blob"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
    
#@+node:tsc.20180209234613.48: *3* sqlite_extract_blob
@g.command('sqlite-extract-blob')
def sqlite_extract_blob(event):    
    
    c = event.get('c')
    
    action = "extract blob"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
    
#@+node:tsc.20180209234613.49: *3* sqlite_open_blob
@g.command('sqlite-open-blob')
def sqlite_open_blob(event):
    
    c = event.get('c')
    
    action = "open blob"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
    
#@+node:tsc.20180209234613.50: *3* sqlite_view_blob
@g.command('sqlite-view-blob')
def sqlite_view_blob(event):
    
    c = event.get('c')
    
    action = "view blob"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
    
#@+node:tsc.20180209234613.51: *3* sqlite_edit_blob
@g.command('sqlite-edit-blob')
def sqlite_edit_blob(event):

    c = event.get('c')
    
    action = "edit blob"
    c._leo4sqlite['action'] = action
    
    InputDialogs(c)
    
#@+node:tsc.20180209234613.52: *3* sqlite_clear_temp
@g.command('sqlite-clear-temp')
def sqlite_clear_temp(event):
    
    c = event.get('c')

    p = g.findNodeAnywhere(c, 'temp')
    if p:
        c.selectPosition(p)
        p.deleteAllChildren()
        c.redraw()
    else:
        pass
#@+node:tsc.20180209234613.53: *3* sqlite_delete_data
@g.command('sqlite-delete-data')
def sqlite_delete_data(event):
    
    c = event.get('c')
    
    p_lst = c.find_h('data')
    
    if p_lst[0]:
        c.selectPosition(p_lst[0])
        p_lst[0].doDelete()
        
    p = c.lastTopLevel().insertAfter()
    c.selectPosition(p)
    p.h = "data"
    c.redraw()
#@+node:tsc.20180209234613.54: *3* sqlite_purge_files
@g.command('sqlite-purge-files')
def sqlite_purge_files(event):
    
    c = event.get('c')
    
    p = g.findNodeAnywhere(c, 'temp')
    c.selectPosition(p)
    p.deleteAllChildren()
    c.redraw()
    
    sqlite_temp_dir = c.config.getString("sqlite_temp_dir")

    os.chdir(sqlite_temp_dir)
    files=glob.glob('*')
    if files:
        for filename in files:
            os.unlink(filename)
#@-others
#@-others
#@@tabwidth -4
#@-leo
