import { Injectable } from '@angular/core';
import { Course } from '@app/classes/course';
import { User } from '@app/classes/user';
import { io, Socket } from 'socket.io-client';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class ClientSocketService {
  socket: Socket;
  id: string = '';
  courses:string[] = [];
  constructor() { 
    this.socket = io(environment.serverUrl, { transports: ['websocket'], upgrade: false });
    this.socket.on('coursesListFound', (list:string) => {
      const tempArray = list.split(", ");
      for (const elem of tempArray) {
        const cleanElem = elem.replaceAll('{','')
          .replaceAll('"','').replaceAll("'","").replaceAll('_',',').replaceAll('->', ' - ').replaceAll('!',"'");
        this.courses.push(cleanElem);
      }
      this.courses.sort();
    });
  }

  getList():void{
    this.socket.emit("getCoursesList");
  }

  sendDataToServer(user:User):void{
    this.socket.emit("launchProcess", user);
  }
}
