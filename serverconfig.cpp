#include <Python.h>
#include <unordered_map>
#include <list>
#include <string>
#include <iostream>
#include <ctime>

class serverconfig{
    std::unordered_map<std::string, userInfo*> members;
    int hostility = 0;
    std::string hostility0 = "Please avoid pinging everyone! Use the correct role pings instead! ^_^";
    std::string hostiliyy1 = "Do not ping @.everyone, please use the correct role pings for this channel";
    std::string hostility2 = "shut the fuck up you bloody imbred ape";

    int tolerance = 5;
    int bantime = 3;
    

    public: bool findUser(std::string id){
        //return members.find(s);
        return !(members.find(id)==members.end());
    }
    public: void addUser(std::string id){
        userInfo* a = new userInfo(id);
        members[id] = a;
    }
    public: void removeUser(std::string id){
        delete(members[id]);
        members.erase(id);
    }


};
class userInfo{
    std::string id;
    std::list <offense> incidents;
    public: userInfo (std::string id){
        this -> id = id;
    }
    public: void addOffense(){
        
    }

};
class offense{

    public: offense(){

    }

};
