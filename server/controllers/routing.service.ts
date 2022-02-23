import { spawn } from 'child_process';
import { Router } from 'express';
import { Service } from 'typedi';

@Service()
export class RoutingService {
  router: Router | undefined;

  constructor() {
      this.configureRouter();
  }

  private configureRouter(): void {
    this.router = Router();

    this.router.get('/', (req, res) => {
      var dataToSend = '';
      // spawn new child process to call the python script
  
      const python = spawn('python', ['script1.py']);
      // collect data from script
          python.stdout.on('data', function (data) {
          console.log('Pipe data from python script ...');
          dataToSend = data.toString();
      });
      
      // in close event we are sure that stream from child process is closed
      python.on('close', (code) => {
          console.log(`child process close all stdio with code ${code}`);
          // send data to browser
          res.send(dataToSend)
      });
    })
    
  }
}
