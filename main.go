package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func getByteData(day int) []byte {
	data, err := ioutil.ReadFile(fmt.Sprintf("data/input%d.txt", day))
	if err != nil {
		log.Fatalf("couldn't read data for day %d: %s", day, err)
	}

	return data
}

func getStringData(day int) string {
	return string(getByteData(day))
}

func main() {
	fmt.Println(getStringData(0))
}
