#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "route.h"

#define VNUM v[55]
#define ANUM a[55]
#define BNUM b[55]
#define CNUM c[55]
#define INFI 555
//设计算法的时候记住，这是一个稀疏图！！！！！！sparse graph！！！
int main()
{	
	int johnson;
	clock_t clk;
	Queue que;
	node graph[600];//图
	int route[600];//储存路径
	int route_in[600],route_out[600];
	int edge_num,node_num;//储存边的数量和点的数量
	int begin,end;//储存起落点
	int v[60], a[60],b[60],c[60];//储存v'的集合,并将其分为A,B,C三个集合
	int i,j,k;//作为循环变量使用
	int val,combo;

	que=(Queue)malloc(sizeof(struct QueueRecord));
	MakeEmpty(que);
	edge_num=read_file_topo("topo1.csv",graph);//读取各条边的数据，存入图中

	{											//读取起点终点和V'，V'存在一维数组里,顺便放入队列，VNUM储存其个数，不另外开变量
		FILE* fp;
		fp=fopen("demand1.csv","r");
		fscanf(fp,"%d",&begin);
		fgetc(fp);
		fscanf(fp,"%d",&end);
		VNUM=0;
		while(!feof(fp))   
    	{	fgetc(fp);
        	fscanf(fp,"%d",&i);
        	Enqueue(i,que);
        	v[VNUM++]=i;
    	}
		fclose(fp);
	}

	//读取完成，开始对点分类	
	ANUM=0;BNUM=0;CNUM=0;
	node_num=graph[555].weight;

	check_a(graph,a,begin,v);
	check_b(graph,b,end,v);

	//分出AB
	for(i=0;i<VNUM;i++)  {
		if (graph[v[i]].kind==0)  c[CNUM++]=v[i];
	}

	//再分出C  
	//下面是把指向begin的路全消掉for(i=0;i<node_num;i++),end指出的路全消
	node_num=graph[555].weight;
	for(i=0;i<node_num;i++)
	{
		for(j=0;j<graph[i].out_num;j++)
		{
			if (graph[i].to_point[j]==begin)
			{

				graph[i].to_point[j]=graph[i].to_point[graph[i].out_num];
				graph[i].out_num--;
			}
		}
	}
	graph[end].out_num=0;

	//准备工作全做好，预加权之类细节先不弄，开始跑！
	//***********************************************
	//目前que内储存着所有V'点
	val=999;
	combo=0;

	for(i=0;i<node_num;i++)  {route_out[i]=0;}//所有点的出度为0
	for(i=0;i<VNUM;i++) route_out[v[i]]=1;	//v'内出度为1
johnson=0;
while(1)
{	johnson++;

	for(i=0;i<node_num;i++)    {route_in[i]=0;route[i]=INFI;}//路径初始化
	//路径初始化
		j=0;
	for(i=0;i<VNUM;i++)
	{	
		k=v[i];
		route[k]=make_random(graph,k);
		route_in[route[k]]++;
		if(route_in[route[k]]>1)  {j=55;break;}

	}//进行V'内所有点的初次随机
	if (j==55)  continue;
	
	route[begin]=make_random(graph,begin);
	route_in[route[begin]]++;
	if(graph[route[begin]].kind==0)  {route[route[begin]]=make_random(graph,route[begin]);route_in[route[route[begin]]]++;}
	//对起点的随机
	for(i=0;i<VNUM;i++)
	{
		
	}
	/*
	for(i=0,j=0;i<node_num;i++) 
	{
		if (route_in[i]>1)  //同一个点有多个入度
		{
			j=55;
			break;
		}
	}
	if (j==55)  continue;*/
	
	for (i=0;i<CNUM;i++)
	{	
		if (route_in[c[i]]!=1) { j=55;break;}//对于C内的点，此时必须已经分配好入度
	}

	if (j==55)  continue;//虽然代码难看，节省了一部分时间
	//此时第一轮取数完成
	//for (i=0;i<VNUM;i++)  {if (route_in[v[i]]==0) printf("%d ",v[i]);}
	//printf("\n");

	


	//printf("%d",graph[7].out_num);

	if((float) clock()>4000) 
		{
			printf("j=%d ",johnson);
			for(i=0;i<VNUM;i++)
			{
			//	printf("%d ",graph[v[i]].out_num);
				
			}
			return 0;
		}




	//以下为最终检查严格合法性，顺便计算最小权的，目前设定为10次combo确定最小
	if (!check_route(begin,end,route,v,graph)) {continue;}
	
	/*i=cost(4,1,graph,route);
	if (i<val) {val=i;combo=0;}
	if (i==val)  combo++;
	if (combo<10)  continue;*/  
	printf("check succeed!!!");
	for(i=begin;i!=end;i=route[i])//粗略测试的时候是用特定点以求通过
	{
		printf("to%d",route[i]);
	}

	printf("cost%d\n",val);
	clk=clock();
	printf("%f\n",(float)clk);


	break;

}
	return 0;
}
//妈的之前那个makeempty buffer 的函数不知道哪里出错了疯狂崩溃，搞了一个多小时！！