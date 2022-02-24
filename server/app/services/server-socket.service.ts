import { User } from "@app/classes/user";
import * as http from "http";
import * as io from "socket.io";
// import { DefaultEventsMap } from "socket.io/dist/typed-events";
import { Service } from "typedi";
const {spawn} = require('child_process');
// declare type Socket = io.Socket<DefaultEventsMap, DefaultEventsMap, DefaultEventsMap>;

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
      console.log(socket.id);

      socket.on("launchProcess", (user: User) => {
        let dataToSend = '';
        const python = spawn('python', ['./python_files/main.py', user.username, user.password, user.dob, user.email, user.courses]);
        python.stdout.on('data', function (data:String) {
          dataToSend = data.toString();
          console.log(dataToSend);
        });
      });
    });
  }
}
