import pandas as pd
import argparse
class Student_search:  #定义学生状态搜索类

    def excel_rtolist(self,path,sheet):#读取excel文件并转为列表
        self.df = pd.read_excel(path , sheet_name = sheet)
        self.name_list = self.df['姓名'].tolist()

    @staticmethod
    def cmdparse(): #增加并读取命令行参数
        parser = argparse.ArgumentParser()
        parser.add_argument("--name" , required = True , help = "要查询的姓名")
        args = parser.parse_args()
        iname = args.name
        return iname

    def name_to_query(self,iname):  #判断人名是否存在
        self.query_name = [n.strip() for n in iname.split(",")]
        self.found_name = [n for n in self.query_name if n in self.name_list]
        self.notfound_name = [n for n in self.query_name if n not in self.name_list]

    def output(self):  #对状态进行输出
        if self.notfound_name:
            print("以下姓名不存在：",",".join(self.notfound_name))
        if self.found_name:
            df = self.df
            result = df.loc[df["姓名"].isin(self.found_name),["姓名", "绿色通道", "财务处",
                                                     "身份核验", "线上报到", "现场报到"]]
            for idx,row in result.iterrows():
                print(f"{row['姓名']}的状态为：")
                print(f"绿色通道：{row['绿色通道']}")
                print(f"财务处：{row['财务处']}")
                print(f"身份核验：{row['身份核验']}")
                print(f"线上报到：{row['线上报到']}")
                print(f"现场报到：{row['现场报到']}")                          
        else:
            print('没有找到这个人')

        input('按回车退出程序')

if __name__ == '__main__':  #测试
    sdsearch = Student_search()
    sdsearch.excel_rtolist(r"C:\Users\Ljh6677\Documents\xwechat_files\wxid_n3qx1lgdjkgp22_9ce3\msg"
        r"\file\2025-08\25智能建造技术2班.xlsx",0)
    iname = sdsearch.cmdparse()
    sdsearch.name_to_query(iname)
    sdsearch.output()
    

        
        
        
