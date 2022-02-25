import { User } from "@app/classes/user";
import * as http from "http";
import * as io from "socket.io";
import { Service } from "typedi";
import { spawn } from 'child_process';

@Service()
export class ServerSocketService {
  sio: io.Server;

  constructor() {}

  initSocket(server: http.Server): void {
    this.sio = new io.Server(server, {
      cors: { origin: "*", methods: ["GET", "POST"] },
    });
  }

  handleSockets(): void {
    this.sio.on("connection", (socket) => {
     
      socket.on("getCoursesList", () =>{
        
        let dataToSend:string = '';
        const python = spawn('python', ['./python_files/transcript_analyser/courses_web_scraper.py']);
        
        python.stdout.on('data', function (data:string) {
          dataToSend = data.toString();
        });
        
        python.on('close', () => {
          socket.emit("coursesListFound", dataToSend);
        });
      });

      socket.on("launchProcess", (user: User) => {
        spawn('python', ['./python_files/main.py', user.username, user.password, user.dob, user.email, user.courses]);
      });
      
    });
  }
}
