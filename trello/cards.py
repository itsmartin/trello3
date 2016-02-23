import json
import requests

class Cards(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, card_id_or_shortlink, actions=None, actions_limit=None, action_fields=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checkItemState_fields=None, checklists=None, checklist_fields=None, board=None, board_fields=None, list=None, list_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, actions=actions, actions_limit=actions_limit, action_fields=action_fields, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checkItemState_fields=checkItemState_fields, checklists=checklists, checklist_fields=checklist_fields, board=board, board_fields=board_fields, list=list, list_fields=list_fields, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_field(self, field, card_id_or_shortlink):
        resp = requests.get("https://trello.com/1/cards/%s/%s" % (card_id_or_shortlink, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_action(self, card_id_or_shortlink, filter=None, fields=None, limit=None, format=None, since=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/cards/%s/actions" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, format=format, since=since, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_attachment(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/attachments" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_board(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/board" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_board_field(self, field, card_id_or_shortlink):
        resp = requests.get("https://trello.com/1/cards/%s/board/%s" % (card_id_or_shortlink, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_checkItemState(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/checkItemStates" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_checklist(self, card_id_or_shortlink, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/checklists" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_list(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/list" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_list_field(self, field, card_id_or_shortlink):
        resp = requests.get("https://trello.com/1/cards/%s/list/%s" % (card_id_or_shortlink, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_member(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/members" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def get_membersVoted(self, card_id_or_shortlink, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/membersVoted" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return resp.json()

    def update(self, card_id_or_shortlink, name=None, desc=None, closed=None, idAttachmentCover=None, idList=None, pos=None, due=None, subscribed=None):
        resp = requests.put("https://trello.com/1/cards/%s" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, closed=closed, idAttachmentCover=idAttachmentCover, idList=idList, pos=pos, due=due, subscribed=subscribed))
        resp.raise_for_status()
        return resp.json()

    def update_checklist_checkItem_name_idCheckList_idCheckItem(self, idCheckList, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/checklist/%s/checkItem/%s/name" % (card_id_or_shortlink, idCheckList, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_checklist_checkItem_po_idCheckList_idCheckItem(self, idCheckList, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/checklist/%s/checkItem/%s/pos" % (card_id_or_shortlink, idCheckList, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_checklist_checkItem_state_idCheckList_idCheckItem(self, idCheckList, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/checklist/%s/checkItem/%s/state" % (card_id_or_shortlink, idCheckList, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_closed(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/closed" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_desc(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/desc" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_due(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/due" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_idAttachmentCover(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/idAttachmentCover" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_idList(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/idList" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_name(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/name" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_po(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/pos" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def update_subscribed(self, card_id_or_shortlink, value):
        resp = requests.put("https://trello.com/1/cards/%s/subscribed" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def new(self, name, idList, desc=None, pos=None, idCardSource=None, keepFromSource=None):
        resp = requests.post("https://trello.com/1/cards" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idList=idList, desc=desc, pos=pos, idCardSource=idCardSource, keepFromSource=keepFromSource))
        resp.raise_for_status()
        return resp.json()

    def new_action_comment(self, card_id_or_shortlink, text):
        resp = requests.post("https://trello.com/1/cards/%s/actions/comments" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(text=text))
        resp.raise_for_status()
        return resp.json()

    def new_attachment(self, card_id_or_shortlink, file=None, url=None, name=None):
        resp = requests.post("https://trello.com/1/cards/%s/attachments" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(file=file, url=url, name=name))
        resp.raise_for_status()
        return resp.json()

    def new_checklist(self, card_id_or_shortlink, value):
        resp = requests.post("https://trello.com/1/cards/%s/checklists" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def new_label(self, card_id_or_shortlink, value, name = None):
        resp = requests.post("https://trello.com/1/cards/%s/labels" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value, name=name))
        resp.raise_for_status()
        return resp.json()

    def new_member(self, card_id_or_shortlink, value):
        resp = requests.post("https://trello.com/1/cards/%s/members" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def new_membersVoted(self, card_id_or_shortlink, value):
        resp = requests.post("https://trello.com/1/cards/%s/membersVoted" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return resp.json()

    def delete(self, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_attachment_idAttachment(self, idAttachment, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/attachments/%s" % (card_id_or_shortlink, idAttachment), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_checklist_idChecklist(self, idChecklist, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/checklists/%s" % (card_id_or_shortlink, idChecklist), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_label_color(self, color, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/labels/%s" % (card_id_or_shortlink, color), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_member_idMember(self, idMember, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/members/%s" % (card_id_or_shortlink, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    def delete_membersVoted_idMember(self, idMember, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/membersVoted/%s" % (card_id_or_shortlink, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return resp.json()

    
