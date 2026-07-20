import { estaciones } from "./data/estaciones";

export default function App() {
  return (
    <div style={{ padding: "30px", fontFamily: "Segoe UI" }}>
      <h1>Dashboard Zona V Cordillera</h1>

      <h2>🚨 Alertas</h2>

      <div
        style={{
          background: "#fee2e2",
          padding: "15px",
          borderRadius: "10px",
        }}
      >
        🔴 EESS 56 La Ligua cerrada por caída de postes eléctricos
      </div>

      <h2 style={{ marginTop: "30px" }}>
        Estado de estaciones
      </h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>FILE</th>
            <th>Comuna</th>
            <th>Estado</th>
          </tr>
        </thead>

        <tbody>
          {estaciones.map((e) => (
            <tr key={e.file}>
              <td>{e.file}</td>
              <td>{e.comuna}</td>
              <td>{e.estado}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
