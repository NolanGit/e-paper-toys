package service

import (
	"fmt"
	"os"
)

func WriteData(text string, fileName string) error {
	cur, err := os.Getwd()
	fmt.Println(cur)
	if err != nil {
		return err
	}
	fmt.Println("%s/resource/%s", cur, fileName)
	file, err := os.Create(fmt.Sprintf("%s/resource/%s", cur, fileName))
	if err != nil {
		return err
	}

	defer file.Close()
	_, err = file.WriteString(text)
	if err != nil {
		return err
	}
	return nil
}
