# last update: Sep 28, 2017
# author: Jin Qu
# contact: jinqu@uw.edu
# programming environment: python3.6


'''                                                                                                                
  ,----..    ,--,                                                                                                  
 /   /   \ ,--.'|                                 ,---,                                                            
|   :     :|  | :      ,---.           ,--,     ,---.'|                                                            
.   |  ;. /:  : '     '   ,'\        ,'_ /|     |   | :                                                            
.   ; /--` |  ' |    /   /   |  .--. |  | :     |   | |                                                            
;   | ;    '  | |   .   ; ,. :,'_ /| :  . |   ,--.__| |                                                            
|   : |    |  | :   '   | |: :|  ' | |  . .  /   ,'   |                                                            
.   | '___ '  : |__ '   | .; :|  | ' |  | | .   '  /  |                                                            
'   ; : .'||  | '.'||   :    |:  | : ;  ; | '   ; |:  |                                                            
'   | '/  :;  :    ; \   \  / '  :  `--'   \|   | '/  '                                                            
|   :    / |  ,   /   `----'  :  ,      .-./|   :    :|                                                            
 \   \ .'   ---`-'             `--`----'     \   \  /                                                              
  `---`   ____                                `----'                                                               
        ,'  , `.                                 ___                                                               
     ,-+-,.' _ |                        ,--,   ,--.'|_                       ,--,                                  
  ,-+-. ;   , ||   ,---.        ,---, ,--.'|   |  | :,'    ,---.    __  ,-.,--.'|         ,---,                    
 ,--.'|'   |  ;|  '   ,'\   ,-+-. /  ||  |,    :  : ' :   '   ,'\ ,' ,'/ /||  |,      ,-+-. /  |  ,----._,.        
|   |  ,', |  ': /   /   | ,--.'|'   |`--'_  .;__,'  /   /   /   |'  | |' |`--'_     ,--.'|'   | /   /  ' /        
|   | /  | |  ||.   ; ,. :|   |  ,"' |,' ,'| |  |   |   .   ; ,. :|  |   ,',' ,'|   |   |  ,"' ||   :     |        
'   | :  | :  |,'   | |: :|   | /  | |'  | | :__,'| :   '   | |: :'  :  /  '  | |   |   | /  | ||   | .\  .        
;   . |  ; |--' '   | .; :|   | |  | ||  | :   '  : |__ '   | .; :|  | '   |  | :   |   | |  | |.   ; ';  |        
|   : |  | ,    |   :    ||   | |  |/ '  : |__ |  | '.'||   :    |;  : |   '  : |__ |   | |  |/ '   .   . |        
|   : '  |/      \   \  / |   | |--'  |  | '.'|;  :    ; \   \  / |  , ;   |  | '.'||   | |--'   `---`-'| |        
;   | |`-'        `----'  |   |/      ;  :    ;|  ,   /   `----'   ---'    ;  :    ;|   |/       .'__/\_: |        
|   ;/                    '---'       |  ,   /  ---`-'                     |  ,   / '---'        |   :    :        
'---'                                  ---`-'                               ---`-'                \   \  /         
  .--.--.                           ___                        ____                                `--`-'          
 /  /    '.                       ,--.'|_                    ,'  , `.                                              
|  :  /`. /                       |  | :,'                ,-+-,.' _ |                                              
;  |  |--`              .--.--.   :  : ' :             ,-+-. ;   , ||                                              
|  :  ;_          .--, /  /    '.;__,'  /     ,---.   ,--.'|'   |  ||                                              
 \  \    `.     /_ ./||  :  /`./|  |   |     /     \ |   |  ,', |  |,                                              
  `----.   \ , ' , ' :|  :  ;_  :__,'| :    /    /  ||   | /  | |--'                                               
  __ \  \  |/___/ \: | \  \    `. '  : |__ .    ' / ||   : |  | ,                                                  
 /  /`--'  / .  \  ' |  `----.   \|  | '.'|'   ;   /||   : |  |/                                                   
'--'.     /   \  ;   : /  /`--'  /;  :    ;'   |  / ||   | |`-'                                                    
  `--'---'     \  \  ;'--'.     / |  ,   / |   :    ||   ;/                                                        
  ,--,          :  \  \ `--'---'   ---`-'   \   \  / '---'                                                         
,--.'|           \  ' ;                      `----'                                                                
|  |,      .--.--.`--`                                                                                             
`--'_     /  /    '                                                                                                
,' ,'|   |  :  /`./                                                                                                
'  | |   |  :  ;_                                                                                                  
|  | :    \  \    `.                                                                                               
'  : |__   `----.   \                                                                                              
|  | '.'| /  /`--'  /                                                                                              
;  :    ;'--'.     /                                                                                               
|  ,   /   `--'---'                        ,---,                                                                   
 ---`-'                                 ,`--.' |                                                                   
  ,----..                        ,--,   |   :  :                                                                   
 /   /   \                     ,--.'|   '   '  ;                                                                   
|   :     :   ,---.     ,---.  |  | :   |   |  |                                                                   
.   |  ;. /  '   ,'\   '   ,'\ :  : '   '   :  ;                                                                   
.   ; /--`  /   /   | /   /   ||  ' |   |   |  '                                                                   
;   | ;    .   ; ,. :.   ; ,. :'  | |   '   :  |                                                                   
|   : |    '   | |: :'   | |: :|  | :   ;   |  ;                                                                   
.   | '___ '   | .; :'   | .; :'  : |__ `---'. |                                                                   
'   ; : .'||   :    ||   :    ||  | '.'| `--..`;                                                                   
'   | '/  : \   \  /  \   \  / ;  :    ;.--,_                                                                      
|   :    /   `----'    `----'  |  ,   / |    |`.                                                                   
 \   \ .'                       ---`-'  `-- -`, ;                                                                  
  `---`                                   '---`"                                                                   
                                                                                                                   
'''

import json
import os
import boto3
import zipfile
import csv
import datetime
import urllib

print('Loading function')


# check if today is Sunday, if so, a weekly cost summary should be included in the email
def IncludeWeeklySummary():
    return datetime.datetime.utcnow().weekday() == 6


### choose which file(s) to parse
'''
    Pick up the most recently updated file;
    Since the cost info of the first day of a month might appear at the cost file of last month,
    for weekly summary, two files will be included.
'''
def FilePicker(contents_list):
    file_list, update_dt = [], []
    for con in contents_list:
        file_name = con['Key'].split('.')
        file_time = con['LastModified']
        if file_name[-1] == 'zip':
            file_list.append(con['Key'])
            update_dt.append(con['LastModified'].timestamp())
    update_dt = sorted(update_dt)
    # check if the current date is within the first 7 days of a month, if so output two most recent files
    # if not, output the most recent files
    current_d = datetime.datetime.utcnow().today().day
    if current_d <= 6:
        idx1, idx2 = update_dt.index(update_dt[-1]), update_dt.index(update_dt[-2])
        file_picked = file_list[idx1], file_list[idx2]
    else:
        idx = update_dt.index(update_dt[-1])
        file_picked = file_list[idx]
    return [file_picked]


# check if the line belongs to today or yesterday's usage
def dayChecker(line_elements, idx_dt):
    '''
    when parsing through the cost info file, this function checks if a certain line contains info of the most recent 24 hrs
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_dt : the index of datetime
    return:
        bool  
    '''
    dt_on_line = line_elements[idx_dt]
    cur_dt = datetime.datetime.utcnow()
    time_elapsed = cur_dt - datetime.datetime.strptime(dt_on_line, '%Y-%m-%d %H:%M:%S')
    updated_last24 = False
    if time_elapsed.days == 0:
        updated_last24 = True
    return updated_last24


# check if the line belongs to the week
def weekChecker(line_elements, idx_dt):
    '''
    when parsing through the cost info file, this function checks if a certain line contains info of the most recent 7 days
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_dt : the index of datetime
    return:
        bool  
    '''
    dt_on_line = line_elements[idx_dt]
    # get current datetime
    cur_dt = datetime.datetime.utcnow()
    # caculate days passed
    time_elapsed = cur_dt - datetime.datetime.strptime(dt_on_line, '%Y-%m-%d %H:%M:%S')
    pick_this_line = False
    if time_elapsed.days <= 6:
        pick_this_line = True
    return pick_this_line


### check if the resource is untagged, if true, print a tag, if not, print False
def untaggedChecker(line_elements, idx_tag1, idx_tag2, idx_tag3, idx_tag4):
    '''
    grab tags
    ---
    arg:    
        array line_elements : a line of a csv file
        int idx_tag1-idx_tag4 : the index of tag
    return:
        if there is a tag, return a string of the tag
        if not return bool False
    '''
    if line_elements[idx_tag1]:
        return line_elements[idx_tag1]
    if line_elements[idx_tag2]:
        return line_elements[idx_tag2]
    if line_elements[idx_tag3]:
        return line_elements[idx_tag3]
    if line_elements[idx_tag4]:
        return line_elements[idx_tag4]
    return False


### aggregate cost by tag and product name
def Agg(line_elements, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend):
    '''
    aggregate blended and unblended cost by product name
    ---
    arg:    
        array line_elements : a line of a csv file
        dict aggs : a dictionary like this: {{tag1: {}}, {tag2: {}}, {tag3: {}}}
        int idx_pname, idx_dollar_blend, idx_dollar_unblend : the index of product name, quantity of blended and unblended cost
    return:
        updated aggs with aggregated cost
    '''
    # product name
    pname = line_elements[idx_pname]
    # cost
    cost_blend = float(line_elements[idx_dollar_blend])
    cost_unblend = float(line_elements[idx_dollar_unblend])
    if tag in aggs:
        aggs[tag]['total_blended_cost'] += cost_blend
        aggs[tag]['total_unblended_cost'] += cost_unblend
        if pname in aggs[tag]:
            aggs[tag][pname]['blended_cost'] += cost_blend
            aggs[tag][pname]['unblended_cost'] += cost_unblend
        else:
            aggs[tag][pname] = {'blended_cost': cost_blend,
                            'unblended_cost': cost_unblend}
            
    else:
        aggs[tag] = {'total_blended_cost': cost_blend,
                     'total_unblended_cost': cost_unblend,
                    pname: {'blended_cost': cost_blend,
                    'unblended_cost': cost_unblend}}



### cost aggregation parser (for daily)
def dailyAgg(file_path):
    '''
    parse through the csv file and generate daily cost summary
    ---
    arg:    
        str file_path : path to the cost file
    return:
        an array contains daily cost summary
        1, dict untagged : {{'resource id 1': $$$}, 'resource id 2': $$$};
        2, dict aggs : {{tag1: {}}, {tag2: {}}, {tag3: {}}};
        3, float total_blend;
        4, float total_unblend;
        5, float total_tagged_blend;
        6, float total_tagged_unblend;
        7, float total_untagged_blend;
        8, float total_untagged_unblend
    '''
    untagged, aggs = {}, {}
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = 0, 0, 0, 0, 0, 0

    with open('/tmp/' + file_path, 'r', newline = '\n') as csvfile:
        lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for idx, line in enumerate(lines):
            if idx == 0:
                col_dict = {}
                for i, n in enumerate(line):
                    col_dict.update({n.strip(): i})
                # get index for tags (user:Name, user:Project)
                idx_tag1, idx_tag2, idx_tag3, idx_tag4 = col_dict['user:Owner'], col_dict['user:Project'], col_dict['user:ProjectName'], col_dict['user:Name']
                # get index for datetime
                idx_dt = col_dict['UsageEndDate']
                # get index for ProductName
                idx_pname = col_dict['ProductName']
                # use quantity has two, blended and unblended
                idx_dollar_blend = col_dict['BlendedCost']
                idx_dollar_unblend = col_dict['UnBlendedCost']
                # for untagged resources
                idx_resource = col_dict['ResourceId']
            else:
                # avoid parse the last few lines
                if line[idx_pname]:
                    if dayChecker(line, idx_dt):
                        tag = untaggedChecker(line, idx_tag1, idx_tag2, idx_tag3, idx_tag4)
                        total_blend += float(line[idx_dollar_blend])
                        total_unblend += float(line[idx_dollar_unblend])
                        if tag:
                            Agg(line, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend)
                            total_tagged_blend += float(line[idx_dollar_blend])
                            total_tagged_unblend += float(line[idx_dollar_unblend])
                        else:
                            total_untagged_blend += float(line[idx_dollar_blend])
                            total_untagged_unblend += float(line[idx_dollar_unblend])

                            if line[idx_resource] in untagged:
                                untagged[line[idx_resource]]['total_blended_cost'] += float(line[idx_dollar_blend])
                                untagged[line[idx_resource]]['total_unblended_cost'] += float(line[idx_dollar_unblend])
                            else:
                                untagged[line[idx_resource]] = {}
                                untagged[line[idx_resource]]['total_blended_cost'] = float(line[idx_dollar_blend])
                                untagged[line[idx_resource]]['total_unblended_cost'] = float(line[idx_dollar_unblend])
    return [untagged, aggs, total_blend, total_unblend, \
            total_tagged_blend, total_tagged_unblend,total_untagged_blend, total_untagged_unblend]


# cost aggregation parser (for weekly)
def weeklyAgg(file_paths):
    '''
    parse through the csv file and generate weekly cost summary
    ---
    arg:    
        str file_path : path to the cost file
    return:
        an array contains daily cost summary
        1, dict untagged : {{'resource id 1': $$$}, 'resource id 2': $$$};
        2, dict aggs : {{tag1: {}}, {tag2: {}}, {tag3: {}}};
        3, float total_blend;
        4, float total_unblend;
        5, float total_tagged_blend;
        6, float total_tagged_unblend;
        7, float total_untagged_blend;
        8, float total_untagged_unblend
    '''
    untagged, aggs = {}, {}
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = 0, 0, 0, 0, 0, 0

    for f in file_paths:
        with open('/tmp/' + f.split('.')[0]+'.csv', 'r', newline = '\n') as csvfile:
            lines = csv.reader(csvfile, delimiter=',', quotechar='"')
            for idx, line in enumerate(lines):
                if idx == 0:
                    col_dict = {}
                    for i, n in enumerate(line):
                        col_dict.update({n.strip(): i})
                    # get index for tags (user:Name, user:Project)
                    idx_tag1, idx_tag2, idx_tag3, idx_tag4 = col_dict['user:Owner'], col_dict['user:Project'], col_dict['user:ProjectName'], col_dict['user:Name']
                    # get index for datetime
                    idx_dt = col_dict['UsageEndDate']
                    # get index for ProductName
                    idx_pname = col_dict['ProductName']
                    # use quantity has two, blended and unblended
                    idx_dollar_blend = col_dict['BlendedCost']
                    idx_dollar_unblend = col_dict['UnBlendedCost']
                    # for untagged resources
                    idx_resource = col_dict['ResourceId']
                else:
                    # avoid parse the last few lines
                    if line[idx_pname]:
                        if weekChecker(line, idx_dt):
                            tag = untaggedChecker(line, idx_tag1, idx_tag2, idx_tag3, idx_tag4)
                            total_blend += float(line[idx_dollar_blend])
                            total_unblend += float(line[idx_dollar_unblend])
                            if tag:
                                Agg(line, aggs, tag, idx_pname, idx_dollar_blend, idx_dollar_unblend)
                                total_tagged_blend += float(line[idx_dollar_blend])
                                total_tagged_unblend += float(line[idx_dollar_unblend])
                            else:
                                total_untagged_blend += float(line[idx_dollar_blend])
                                total_untagged_unblend += float(line[idx_dollar_unblend])

                                if line[idx_resource] in untagged:
                                    untagged[line[idx_resource]]['total_blended_cost'] += float(line[idx_dollar_blend])
                                    untagged[line[idx_resource]]['total_unblended_cost'] += float(line[idx_dollar_unblend])
                                else:
                                    untagged[line[idx_resource]] = {}
                                    untagged[line[idx_resource]]['total_blended_cost'] = float(line[idx_dollar_blend])
                                    untagged[line[idx_resource]]['total_unblended_cost'] = float(line[idx_dollar_unblend])
        return untagged, aggs, total_blend, total_unblend, \
                total_tagged_blend, total_tagged_unblend,total_untagged_blend, total_untagged_unblend


### friendly print out aggregated cost
def BeautifulPrint(aggs, untagged, is_weekly_summary, *all_costs):
    '''
    give the cost summary generated by func dailyAgg or weeklyAgg, 
    output a reader-friendly string 
    ---
    arg:    
        1, dict aggs : {{tag1: {}}, {tag2: {}}, {tag3: {}}};
        2, dict untagged : {{'resource id 1': $$$}, 'resource id 2': $$$};
        3, bool is_weekly_summary : True/False;
        4, *all_costs : float total_blend, float total_unblend, float total_tagged_blend, 
                        float total_tagged_unblend, float total_untagged_blend, float total_untagged_unblend
    return:
        str cost_summary
    '''
    total_blend, total_unblend, total_tagged_blend, total_tagged_unblend, \
    total_untagged_blend, total_untagged_unblend = [*all_costs]
    cur_time = datetime.datetime.utcnow()
    
    # dictionary for substituting full name with shorter name
    resource_name_map = {'Amazon Elastic Compute Cloud': 'EC2', 'Amazon Simple Storage Service': 'S3'}
    
    cost_agg = ' '
    
    if is_weekly_summary:
        cost_agg += 'HPCCloud spend = ${}(${}) from {} to {} \n'.format(str(round(total_tagged_blend, 2)), str(round(total_untagged_blend, 2)),
                                                                    datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - 86400.0 * 7)).strftime('%Y-%m-%d %H:%M:%S') + \
                                                                     ' UTC to ', cur_time.strftime('%Y-%m-%d %H:%M:%S') + ' UTC ')
    else:
        cost_agg += 'HPCCloud spend = ${}(${}) from {} to {} \n'.format(str(round(total_tagged_blend, 2)), str(round(total_untagged_blend, 2)),
                                                                    datetime.datetime.fromtimestamp(int(datetime.datetime.utcnow().timestamp() - 86400.0)).strftime('%Y-%m-%d %H:%M:%S') + \
                                                                     ' UTC to ', cur_time.strftime('%Y-%m-%d %H:%M:%S') + ' UTC ')
    cost_agg += '~ '*10 
    cost_agg += '\n'
    
    cost_agg += 'Total: ${blend}\n'.format(blend = str(round(total_blend, 2)))
        
    cost_agg += 'Tagged ${blend}\n'.format(blend = str(round(total_tagged_blend, 2)))
        
    cost_agg += 'Untagged ${blend}\n'.format(blend = str(round(total_untagged_blend, 2)))
    
    cost_agg += '~ ' * 10
    
    cost_agg += '\n Details: \n'
                                                                                                     
    for k1, v1 in aggs.items():
        cost_agg += '{tag}{blend}\n'.format(tag='Tag: '+k1, 
                                            blend='\t Total: $' + str(round(v1['total_blended_cost'], 2)) + ', ')
        for k2, v2 in v1.items():
            if k2 not in ['total_blended_cost', 'total_unblended_cost']:
                cost_agg += '{resource} '.format(resource = resource_name_map[k2] if resource_name_map.get(k2) else k2)
                kv3 = list(v2.items())
                cost_agg += '{cost1}\n'.format(cost1 = ': $'+str(round(kv3[0][1], 2)))
                    
        cost_agg += ('-'*10 + '\n')
        
    cost_agg += 'Cost with untagged resources: \n' + '~ ' * 10 + '\n'
    for k, v in untagged.items():
        cost_agg += '{id:}'.format(id = 'ResourceID(if any): ' + k + '\n')
        cost_agg += '{blend}\n'.format(blend='Total: $' + str(round(v['total_blended_cost'], 2)) + ', ')
        cost_agg += '----------\n'
    
    return cost_agg
    

### catches S3 update event and fires aggregation parser   
def lambda_handler(event, context):
    '''
    catches S3 update event, parse cost info and send cost summary to SSN, which will send email notifications
    ---
    arg:    
        1, list event
        2, list context
    return:
        None
    '''
    # print("Received event: " + json.dumps(event, indent=2))
    s3 = boto3.client('s3', aws_access_key_id='xxx', aws_secret_access_key='xxx')
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # list objects
        obj_list = s3.list_objects(Bucket = bucket)
        
        # response2 = s3.get_object(Bucket=bucket, Key = obj_list['Contents'][1]['Key'])
        s3_resource = boto3.resource('s3')
        # s3_resource.Object(bucket, obj_list['Contents'][1]['Key']).download_file('/tmp/'+obj_list['Contents'][1]['Key'])
        files_for_parse = FilePicker(obj_list['Contents'])
        
        print(files_for_parse)

        for f in files_for_parse:
            s3_resource.Object(bucket, f).download_file('/tmp/' + f)
            zip_ref = zipfile.ZipFile('/tmp/'+ f, 'r')
            zip_ref.extractall('/tmp/')
        
        # print(os.listdir('/tmp/'))

        # read and process the most recently updated file
        file_for_daily_agg = files_for_parse[0]

        daily_untagged, daily_aggs, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, \
        daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend = dailyAgg(file_for_daily_agg.split('.')[0]+'.csv')
        
        # print(aggs)
        # print('---------\n')
        # print(untagged)
        
        cost_agg_str = BeautifulPrint(daily_aggs, daily_untagged, False, daily_total_blend, daily_total_unblend, daily_total_tagged_blend, 
               daily_total_tagged_unblend, daily_total_untagged_blend, daily_total_untagged_unblend)

        if IncludeWeeklySummary():
            weekly_untagged, weekly_aggs, weekly_total_blend, weekly_total_unblend, \
            weekly_total_tagged_blend, weekly_total_tagged_unblend, weekly_total_untagged_blend, \
            weekly_total_untagged_unblend = weeklyAgg(files_for_parse)

            weekly_cost_agg_str = BeautifulPrint(weekly_aggs, weekly_untagged, True, weekly_total_blend, weekly_total_unblend, 
                weekly_total_tagged_blend, weekly_total_tagged_unblend, weekly_total_untagged_blend, weekly_total_untagged_unblend)

            cost_agg_str += ('\n' + '-'*10)
            cost_agg_str += ('\n ~~~ weekly cost summary: ~~~ \n' + weekly_cost_agg_str)

        sns = boto3.client('sns', aws_access_key_id='xxx', aws_secret_access_key='xxx')
        response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:xxxxxx',
        Message=cost_agg_str,
        Subject='Daily Cloud Computing Cost Summary')
        
        return 'completed!'
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
