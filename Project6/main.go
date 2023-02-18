// Name: Edward E. Daisey
// Date: February 17, 2023
// Purpose: Go practice.


package main

import (
     "fmt"
     "os"
     "io/ioutil"
     "gopkg.in/yaml.v2"
 )

type Config struct {
     Username string 'yaml:"name"'
     Host     string 'yaml:"hosts"'
}

func main(){
     // Purpose - Read the configuration file.
     configData, err := ioutil.ReadFile("config.yaml")
     if err != nil {
          fmt.Println("Error reading config file:", err)
	  os.Exit(1)
     }

     // Purpose - Parse the configuration file.
     var config Config
     err = yaml.Unmarshal(configData, &config)
     if err != nil {
         fmt.Println("Error parsing config file:", err)
	 os.Exit(1)
     }

     fmt.Println("Username: ", config.Username)
     fmt.Println("Host: ", config.Host)
}