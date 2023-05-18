class Queue {
    constructor(){
        this.elements = {};
        this.head = 0;
        this.tail = 0;
    }

    enqueue(data){
        this.elements[this.tail] = data
        this.tail++
    }

    dequeue(){
        delete this.elements[this.head]
        this.head++
    }

    peek(){
        return this.elements[this.head]
    }

    isEmpty(){
        return this.tail == 0
    }

    get size(){
        return this.tail - this.head
    }
}