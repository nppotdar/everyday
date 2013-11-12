def towersOfHanoi(source, destination, intermediate, n):
    if n == 2:
        print "Moving from ", source, " to ", intermediate
        print "Moving from ", source, " to ", destination
        print "Moving from ", intermediate, " to ", destination
        return
    towersOfHanoi(source, intermediate, destination, n-1)
    print "Moving from ", source, " to ", destination
    towersOfHanoi(intermediate, destination, source, n-1)

if __name__ == "__main__":
    towersOfHanoi("A", "C", "B", 3)
        
