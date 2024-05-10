
import os,logging,subprocess
logging.basicConfig(level=logging.DEBUG ,format="%(asctime)s\t%(levelname)s\t%(filename)s  %(funcName)s:%(lineno)d\t%(message)s")

from datetime import datetime

folder = os.path.split(os.path.realpath(__file__))[0]

out_folder = folder + "/../_posts"
logging.debug('%s',out_folder)

# os.system("rm -rf "+out_folder)
os.system("mkdir -p "+out_folder)



posts_info={'null':['null']}

def get_last_commit_time(file_path):
    try:
        # 使用 subprocess 调用 git log 命令并捕获输出
        output = subprocess.check_output(["git", "log", "-n", "1", '--format=%ad', "--", file_path])
        # output = subprocess.check_output(["git", "status"])

        # 将输出解码为字符串，并移除末尾的换行符
        last_commit_time_str = output.decode("utf-8").strip()
        
        # 将字符串解析为 datetime 对象
        last_commit_time = datetime.strptime(last_commit_time_str, "%a %b %d %H:%M:%S %Y %z")

        # 将 datetime 对象格式化为指定格式的字符串
        formatted_time = last_commit_time.strftime("%Y-%m-%d %H:%M:%S %z")
        
        return last_commit_time
    except subprocess.CalledProcessError:
        # 如果命令执行失败，则返回 None
        return None

def HandleFile(filename:str,shortname:str):
    f = open(filename,"r+",1024,'utf-8')
    lines = f.readlines()
    f.close()
    
    
    last_commit_time = get_last_commit_time(filename)
    if last_commit_time == None:
        logging.warning("%s",'cant get last commit time')
        return
    if posts_info.get(shortname) == None:
        logging.warning("%s",'cant get info')
        logging.warning(posts_info)
        return
    
    header='--- \n layout: post'
    header+= '\ntitle: "'+shortname.replace('.md','')+'"'
    header+= '\ndate: '+last_commit_time.strftime("%Y-%m-%d %H:%M:%S %z")
    header+= '\ncategories:  [ '+', '.join(posts_info[shortname]) + ' ]'
    header+='\n--- \n'
    

    
    lines.insert(0,header)
    logging.debug('%s', filename)
    
    f = open(out_folder+'/'+last_commit_time.strftime("%Y-%m-%d-")+shortname,"w+",1024,'utf-8')
    f.writelines(lines)
    f.close()

def GetInfo(find_path:str,info=[]):
    global posts_info
    for item in os.listdir(find_path):
        # check if current path is a file
        p = os.path.join(find_path, item)
        if os.path.isfile(p) & (item.count('.md')):
            posts_info[item] = info.copy()
            logging.debug(posts_info)
            HandleFile(p,item)
        elif os.path.isdir(p):
            info.append(item) 
            logging.debug(info)
            GetInfo(p,info)
            info.pop()
            
GetInfo(folder)
logging.info(posts_info)