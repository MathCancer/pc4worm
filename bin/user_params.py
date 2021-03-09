 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Initialization settings---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='number_of_cells', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.number_of_cells = IntText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        param_name3 = Button(description='attachment_elastic_constant', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.attachment_elastic_constant = FloatText(
          value=0.03,
          step=0.001,
          style=style, layout=widget_layout)

        param_name4 = Button(description='head_migration_direction', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.head_migration_direction = FloatText(
          value=-1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='head_migration_speed', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.head_migration_speed = FloatText(
          value=0.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='head_migration_bias', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.head_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='head_migration_persistence', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.head_migration_persistence = FloatText(
          value=60,
          step=1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='tail_migration_direction', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.tail_migration_direction = FloatText(
          value=-1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='tail_migration_speed', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.tail_migration_speed = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name10 = Button(description='tail_migration_bias', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.tail_migration_bias = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='tail_migration_persistence', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.tail_migration_persistence = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name12 = Button(description='middle_migration_speed', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.middle_migration_speed = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'lightgreen'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'tan'
        units_button6 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='initial number of cells (for each cell type)' , tooltip='initial number of cells (for each cell type)', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='strength of the spring-like adhesion for attached cells' , tooltip='strength of the spring-like adhesion for attached cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='+1: grad(signal). -1: -grad(signal)' , tooltip='+1: grad(signal). -1: -grad(signal)', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='migration speed for head cells' , tooltip='migration speed for head cells', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='migration bias for head cells' , tooltip='migration bias for head cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='migration persistence time for head cells' , tooltip='migration persistence time for head cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='+1: grad(signal). -1: -grad(signal)' , tooltip='+1: grad(signal). -1: -grad(signal)', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='migration speed for tail cells' , tooltip='migration speed for tail cells', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='migration bias for tail cells' , tooltip='migration bias for tail cells', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='migration persistence time for tail cells' , tooltip='migration persistence time for tail cells', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='migration speed of middle cells, along grad(signal)' , tooltip='migration speed of middle cells, along grad(signal)', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.number_of_cells, units_button3, desc_button2] 
        row3 = [param_name3, self.attachment_elastic_constant, units_button4, desc_button3] 
        row4 = [param_name4, self.head_migration_direction, units_button5, desc_button4] 
        row5 = [param_name5, self.head_migration_speed, units_button6, desc_button5] 
        row6 = [param_name6, self.head_migration_bias, units_button7, desc_button6] 
        row7 = [param_name7, self.head_migration_persistence, units_button8, desc_button7] 
        row8 = [param_name8, self.tail_migration_direction, units_button9, desc_button8] 
        row9 = [param_name9, self.tail_migration_speed, units_button10, desc_button9] 
        row10 = [param_name10, self.tail_migration_bias, units_button11, desc_button10] 
        row11 = [param_name11, self.tail_migration_persistence, units_button12, desc_button11] 
        row12 = [param_name12, self.middle_migration_speed, units_button13, desc_button12] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.number_of_cells.value = int(uep.find('.//number_of_cells').text)
        self.attachment_elastic_constant.value = float(uep.find('.//attachment_elastic_constant').text)
        self.head_migration_direction.value = float(uep.find('.//head_migration_direction').text)
        self.head_migration_speed.value = float(uep.find('.//head_migration_speed').text)
        self.head_migration_bias.value = float(uep.find('.//head_migration_bias').text)
        self.head_migration_persistence.value = float(uep.find('.//head_migration_persistence').text)
        self.tail_migration_direction.value = float(uep.find('.//tail_migration_direction').text)
        self.tail_migration_speed.value = float(uep.find('.//tail_migration_speed').text)
        self.tail_migration_bias.value = float(uep.find('.//tail_migration_bias').text)
        self.tail_migration_persistence.value = float(uep.find('.//tail_migration_persistence').text)
        self.middle_migration_speed.value = float(uep.find('.//middle_migration_speed').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//number_of_cells').text = str(self.number_of_cells.value)
        uep.find('.//attachment_elastic_constant').text = str(self.attachment_elastic_constant.value)
        uep.find('.//head_migration_direction').text = str(self.head_migration_direction.value)
        uep.find('.//head_migration_speed').text = str(self.head_migration_speed.value)
        uep.find('.//head_migration_bias').text = str(self.head_migration_bias.value)
        uep.find('.//head_migration_persistence').text = str(self.head_migration_persistence.value)
        uep.find('.//tail_migration_direction').text = str(self.tail_migration_direction.value)
        uep.find('.//tail_migration_speed').text = str(self.tail_migration_speed.value)
        uep.find('.//tail_migration_bias').text = str(self.tail_migration_bias.value)
        uep.find('.//tail_migration_persistence').text = str(self.tail_migration_persistence.value)
        uep.find('.//middle_migration_speed').text = str(self.middle_migration_speed.value)
