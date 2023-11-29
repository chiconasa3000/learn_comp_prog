#include <iostream>
using namespace std;
// Definition fo singly-linked list
struct ListNode{
	int val;
	ListNode *next;

	ListNode() : val(0), next(nullptr){}
	ListNode(int x): val(x), next(nullptr){}
	ListNode(int x, ListNode *next) : val(x), next(next){}
	
	ListNode(int samples[],int n){
		ListNode *head = new ListNode(samples[0]);
		ListNode *chead = head;
	
		int nums_size = n;
		for(int i=1; i<nums_size; ++i){
			ListNode *next = new ListNode(samples[i]);
			if(i==1) (*chead).next = next;
			(*head).next = next;
			head = next;
		}
		(*this).val = (*chead).val;
		(*this).next = (*chead).next;
	}	
	
	int get_size(){
		ListNode *dp = new ListNode(this->val,this->next);
		int cont = 0;
		while(dp != nullptr){
			cont++;
			dp = dp->next;
		}
		return cont;
	}	
	void print(int items){
		ListNode *dp = new ListNode(this->val,this->next);
		cout << "[ ";
		while(dp != nullptr){	
			cout << dp->val << " ";
			dp = dp->next;
		}
		cout << "]\n";
	}

};

int get_size(ListNode *h){
	ListNode *dp = new ListNode(h->val,h->next);
	int cont = 0;
	while(dp != nullptr){
		cont++;
		dp = dp->next;
	}
	return cont;
}	

ListNode* middleNode(ListNode* head){
	ListNode *t = new ListNode(head->val, head->next);
	int size_list = get_size(head);
	int times = 0;
	times = size_list / 2 + 1;
	cout << "times: " << times << "\n";
	for(int i=1; i<times; i++){
		t = t->next;
	}
	return t;	
}
		
int main()
{
	int nums[] {1,2,3,4,5};
	int nums_size = sizeof(nums)/sizeof(int);
	ListNode *hh = new ListNode(nums,nums_size);
	ListNode *p = middleNode(hh);	
	cout << p->val << "\n";
	return 0;
}
