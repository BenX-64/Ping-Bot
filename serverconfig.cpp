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
    public:

    bool checkUser(std::string s){
        //return members.find(s);
        return false;
    }
    void addUser(std::string s){
        userInfo* a = new userInfo();
        members[s] = a;
    }
    void removeUser(std::string s){
        delete(members[s]);
        members.erase(s);
    }


};
class userInfo{
    std::string id;
    
    public:
};
class offenses{
    public:

};
