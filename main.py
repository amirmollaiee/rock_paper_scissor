#!/usr/bin/python
import random as rn 

class rpc:
    list_object=["paper","rock","scissor"]
    pc_score=0
    user_score=0
    def __init__(self,user):
        self.username=user
    def choice_object(self):
        choice=rn.choice(rpc.list_object)
        return choice
    def user_answer(self):
        answer=input("pleas enter you choices : ")
        return answer
    def compare(self):
        while True:
            pc=rpc.choice_object(self)
            user=rpc.user_answer(self)
            if pc == user :
                print("equal")
            elif pc == "paper" and user == "rock":
                rpc.pc_score+=1
                print("pc win")
            elif pc == "paper" and user == "scissor":
                rpc.user_score+=1
                print("user win")
            elif pc == "rock" and user == "paper":
                rpc.user_score+=1
                print("user win")
            elif pc == "rock" and user == "scissor":
                rpc.pc_score+=1
                print("pc win")
            elif pc == "scissor" and user == "rock":
                rpc.user_score+=1
                print("user win")
            elif pc == "scissor" and user == "paper":
                rpc.pc_score+=1
                print("pc win")
            elif user== "exit":
                break
            elif user == "help" or user == "h":
                txt="""
                this rock paper scissor game
                rock 
                paper 
                scissor
                exit   this comand exit the program 
                score   show the score of the player
                """
                print(txt)
            elif user == "score":
                print("you: ",rpc.user_score,"--","pc: ",rpc.pc_score)
            else:
                print("this command is not found")
                
        
        


app=rpc("amir")
app.compare()



