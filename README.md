# 6cloud_cmdb平台

## 资源管理
### 主机管理
* 主机 （主机组、主机拓扑）(注册到堡垒机、注册监控)
* 机房 （机房-机柜拓扑）
* 机柜 （机柜-主机拓扑）
### 进程管理
### 服务管理
### docker镜像

## 业务管理
### 业务拓扑

## 应用管理

## 用户和权限管理

## 审计
### 变更记录
### 操作日志

# 6cloud_ci_cd平台
* Gitlab(checkout branch) -> Jenkins(push image) -> Harbor(pull image)
-> K8s(deploy) <- Spinnaker、HELM、Kubectl/YAML