from sym_api_client_python.listeners.RoomListener import RoomListener
import calendar;
import time;
import logging
import messageParse
from nlp import nlpMain
import requests
import callDB

#sample implementation of Abstract RoomListener class
#has instance of SymBotClient so that it can respond to events coming in by leveraging other clients on SymBotClient
#each function should contain logic for each corresponding event
class RoomListenerTestImp(RoomListener):

    def __init__(self, SymBotClient):
        self.botClient = SymBotClient

    def onRoomMessage(self, message):
        logging.debug('room message recieved', message)
        #sample code for developer to implement --> use MessageClient and
        #data recieved from message event to reply with a #reed
        m = messageParse.messageParse(message)
        content = m.getContent()
        streamId = message['stream']['streamId']
        print(content)
        nlp = nlpMain.NLPMain(content)
        nlpobj = nlp.extractMeaning()
        callobj = callDB.callDB(nlpobj)
        finalRes = callobj.call()
        message = dict(message = '<messageML>'+finalRes+'</messageML>')
        self.botClient.getMessageClient().sendMessage(streamId, message)

    def onRoomCreated(self, roomCreated):
        logging.debug('room created', roomCreated)

    def onRoomDeactivated(self, roomDeactivated):
        logging.debug('room Deactivated', roomDeactivated)

    def onRoomMemberDemotedFromOwner(self, roomMemberDemotedFromOwner):
        logging.debug('room member demoted from owner', roomMemberDemotedFromOwner)

    def onRoomMemberPromotedToOwner(self, roomMemberPromotedToOwner):
        logging.debug('room member promoted to owner', roomMemberPromotedToOwner)

    def onRoomReactivated(self, roomReactivated):
        logging.debug('room reactivated', roomReactivated)

    def onRoomUpdated(self, roomUpdated):
        logging.debug('room updated', roomUpdated)

    def onUserJoinedRoom(self, userJoinedRoom):
        logging.debug('USER JOINED ROOM', userJoinedRoom)

    def onUserLeftRoom(self, userLeftRoom):
        logging.debug('USER LEFT ROOM', userLeftRoom)
