#---------------------Wechat_Config-------------------------------------------------------------------------------

appID = "wx014e6d2d5edeef3e"
appSecret = "f66d2b19071fd42f0b30a45985a5b518"

#Receiver ID
openId = "oN8Uu65PgzXqHrMMrHXZ3tst78bA"

# Templete ID : Premium
timetable_template_id = "nwhiLPwuZWNiRpSY5l9ehJg06COdDoo3ybQu6tp4EbQ" 

#------------------------------------------------------------------------------------------------------------------

#This is the python file used to define the command executing in Linux


#------------------Defination of the infra commands-----------------------------------------------------------------


#This command functioned to mount the M4 elf file
cmd_mnt    = "echo /usr/local/projects/Test_CM4/lib/firmware/Test_CM4.elf > /sys/class/remoteproc/remoteproc0/firmware"

#This command functioned to start the M4 elf file which has been mounted before
cmd_start  = "echo start > /sys/class/remoteproc/remoteproc0/state"

#This command functioned to stop the M4 elf file
cmd_stop   = "echo stop > /sys/class/remoteproc/remoteproc0/state"

#This command functioned to open the /dev/ttyRPMSG0 protocol
cmd_open   = """echo "1" > /dev/ttyRPMSG0"""

#This command functioned to get the state of the M4 offline/running
cmd_check  = "cat /sys/class/remoteproc/remoteproc0/state"


#--------------------------------------------------------------------------------------------------------------------



#------------------Defination of the perpherial commands-------------------------------------------------------------


LED_ON                =   "LED_ON"
LED_OFF               =   "LED_OFF"


#--------------------------------------------------------------------------------------------------------------------



#------------------Programmer Function commands----------------------------------------------------------------------

Init                  =   "Init"
Shutdown              =   "Shutdown"