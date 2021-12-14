#!/usr/bin/env python3
class event():
    def __init__(self, name = ""):
        self.name = name
        self.data_dic = {}
        self.index = -1

    class Struct():
        def __init__(self, Id, message, Type):
            self.Id = Id
            self.Type = Type
            self.StartTime = StartTime
            self.latencies = latencies
            self.message = message
            self.status = status
            #self.line_num = num
    #return struct item.
    def newEvent(self, name, message  ):
        return self.Struct( name, message )

if __name__ == "__main__":
    En = event()
    messageGen=En.newEvent(1,"gen",1)
    send=En.newEvent(2,"send",2)
