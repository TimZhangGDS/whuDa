# -*- coding: utf-8 -*-
from whuDa import db
'''question_invite_id int(11) unsigned not null auto_increment comment '����ID',
    question_id int(11) not null comment '����ش������ID',
    sender_uid int(11) not null comment '����������û�UID',
    recipient_uid int(11) not null comment '��������û�UID',
    send_time int(10) not null comment '���뷢��ʱ��',
    primary key(question_invite_id)'''
class Question_invite:
	question_invite_id=db.Column(db.Integer, primary_key=True);
	question_id=db.Column(db.Integer,nullable=False);
	sender_uid=db.Column(db.Integer,nullable=False);
	recipient_uid=db.Column(db.Integer,nullable=False);
	send_time=db.Column(db.Integer,nullable=False);