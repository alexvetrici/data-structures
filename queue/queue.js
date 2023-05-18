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

var q = new Queue()
console.log(q.isEmpty())
q.enqueue(5)
q.enqueue(43)
q.enqueue(78)
console.log(q)
console.log(q.peek())
q.dequeue()
q.dequeue()
console.log(q.size)
console.log(q.peek())
console.log(q)
