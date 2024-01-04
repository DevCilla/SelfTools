create table db.tablename
(
    qNo              int                                  not null comment 'question number',
    objective        varchar(100)                         not null comment 'topic of the question',
    isCorrect        tinyint(1) default 0                 not null comment 'correct or wrong',
    qId              varchar(7)                           not null comment 'question id used to trace the question on the website ',
    created_datetime datetime   default CURRENT_TIMESTAMP not null,
    id               int auto_increment comment 'primary key'
        primary key,
    batch            varchar(20)                          not null comment 'batch no. of the practise test',
    constraint practice_result_pk
        unique (id)
)
    collate = utf8mb4_unicode_ci;

