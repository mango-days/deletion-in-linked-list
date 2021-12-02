class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
            
    def delete ( self , a ) :
        if self.head.data != a :
            find_a = self.head
            prev_a = self.head
            while ( find_a.data != a ) :
                prev_a = find_a
                find_a = find_a.next
        
            prev_a.next = find_a.next
            find_a.next = None
        elif self.head.next != None : self.head = self.head.next
        else : self.head = None
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 3 )
llist.add ( 4 )
llist.add ( 5 )
llist.delete ( 1 )
llist.printList()