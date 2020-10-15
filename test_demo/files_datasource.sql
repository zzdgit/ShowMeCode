/*
Navicat PGSQL Data Transfer

Source Server         : 54
Source Server Version : 100600
Source Host           : 10.200.60.54:5432
Source Database       : zzd_test
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 100600
File Encoding         : 65001

Date: 2020-07-10 16:01:58
*/


-- ----------------------------
-- Table structure for files_datasource
-- ----------------------------
DROP TABLE IF EXISTS "public"."files_datasource";
CREATE TABLE "public"."files_datasource" (
"id" int4 DEFAULT nextval('files_datasource_id_seq'::regclass) NOT NULL,
"user" varchar(512) COLLATE "default",
"user_name" varchar(512) COLLATE "default",
"name" varchar(128) COLLATE "default" NOT NULL,
"data_set" varchar(128) COLLATE "default",
"description" varchar(256) COLLATE "default",
"type" varchar(16) COLLATE "default" NOT NULL,
"size" varchar(32) COLLATE "default",
"status" varchar(16) COLLATE "default" NOT NULL,
"path" varchar(512) COLLATE "default" NOT NULL,
"download_url" varchar(512) COLLATE "default",
"create_time" timestamptz(6) NOT NULL,
"is_delete" bool NOT NULL,
"update_time" timestamptz(6),
"row_num" int4,
"column_num" int4,
"dtypes" text COLLATE "default",
"is_deeplearning" bool NOT NULL,
"project_id" varchar(128) COLLATE "default",
"is_share" bool NOT NULL,
"bucket_name" varchar(16) COLLATE "default",
"minio_file_name" varchar(128) COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table files_datasource
-- ----------------------------
ALTER TABLE "public"."files_datasource" ADD PRIMARY KEY ("id");
