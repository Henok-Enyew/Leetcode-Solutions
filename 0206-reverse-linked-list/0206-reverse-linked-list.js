function reverseList(head){
    let currentNode =null;
    while(head){
        const temp = head.next;
        head.next = currentNode;
        currentNode = head;
        head = temp;
    }

    return currentNode;
}